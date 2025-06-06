# Using content protection systems with HLS

**Framework**: HTTP Live Streaming

Adding encryption keys to media playlists

#### Overview

HTTP Live Streaming (HLS) supports content protection systems through the presence of `EXT-X-KEY` tags in playlists. HLS allows multiple `EXT-X-KEY` tags with diﬀerent `KEYFORMAT` attributes to apply to the same segments provided that each of the tags ultimately produces the same decryption key. This is necessary because you can only encrypt a media segment with one encryption method, using one encryption key, with a single IV (initialization vector).

While a playlist may contain `EXT-X-KEY` tags for more than one protection system, a player typically supports only one protection system. This means that every encrypted segment must have `EXT-X-KEY` tags for the same set of protection systems. The player refuses to play the playlist if it doesn’t handle any of the protection systems. If the player can handle more than one protection system, it chooses one. The playlist has no mechanism to convey a preference for a protection system.

This document provides general guidance on using such `EXT-X-KEY` tags.

For convenience sake, this document refers to some details of the Google Widevine and Microsoft PlayReady protection systems. The documentation for those systems should be used to ensure accurate implementation.

#### Set the Playlist Key Tag

The `EXT-X-KEY` tag has three attributes that principally control its behavior. These are `METHOD`, `KEYFORMAT`, and `URI`.

#### Choose a Key Format

There are four supported key formats:

- Identity
- FairPlay Streaming
- Widevine
- PlayReady

All formats (except Identity) require a key server. That is, a server that uses some protocol to supply the keys. The key server isn’t specified by the playlist. Instead, the playback app is responsible for knowing the URI of the key server and the protocol for communicating with that server.

##### Identity

This format is identified by a `KEYFORMAT` attribute with the value `identity` or by the lack of a `KEYFORMAT` attribute.

The `URI` attribute is the URI of the key file.

Because there is no key server involved, this protection system aﬀords only a minimal level of protection. For that reason you shouldn’t use identity keys in conjunction with any other protection system.

This format is described in [`HTTP Live Streaming 2nd Edition`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis)

##### Fairplay Streaming

This format is identified by a `KEYFORMAT` attribute with the value `com.apple.streamingkeydelivery`.

The `URI` attribute typically has the form `skd://<key-identifier>`. (In theory this can use any custom URL scheme, but `skd` is almost always used.) The key-identifier is an arbitrary string that is interpreted by the FairPlay Key Server. FairPlay does impose limits on the overall length of the key-identifier string.

Further details about FairPlay Streaming are available at [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/).

##### Widevine

The Widevine format has more than one version. However, the versions use diﬀerent key format values; from the HLS point of view, they are completely distinct. You should use what the Widevine documentation refers to as v2.

This key format is identified by a `KEYFORMAT` attribute with the value `urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed`. (The UUID in this URN is the Widevine System ID. See [`Widevine PSSH data`](using-content-protection-systems-with-hls#Widevine-PSSH-data.md).)

The `URI` attribute has the form `data:text/plain;base64,<base64 encoded PSSH box>`. See [`Create a PSSH box`](using-content-protection-systems-with-hls#Create-a-PSSH-box.md).

For more information about Widevine refer to [`Widevine Technologies`](https://developer.apple.comhttps://www.widevine.com).

##### Playready

The PlayReady format is defined by Microsoft.

This key format is identified by a `KEYFORMAT` attribute with the value `com.microsoft.playready`.

The `URI` has the form `data:text/plain;charset=UTF-16;base64,<base64 encoded PlayReady Object>`. See [`PlayReady PSSH data`](using-content-protection-systems-with-hls#PlayReady-PSSH-data.md) for a discussion of the PlayReady Object.

For more information refer to the [`PlayReady documentation`](https://developer.apple.comhttps://learn.microsoft.com/en-us/playready/).

#### Select Key Identifiers

All three of the key formats that use a key server - FairPlay Streaming, Widevine, PlayReady - contain something called a key identifier. The key identifier is the data sent to the server so it can return the correct key.

The FairPlay Streaming key identifier has no relationship to that used by the other formats.

The Widevine and PlayReady key identifiers may be identical. Their value should be a UUID. Note that PlayReady does not store the UUID as a simple 16-byte array. (See the [`Example`](using-content-protection-systems-with-hls#Example.md) below for more detail.)

#### Create a Pssh Box

The Protection System Specific Header (‘pssh’) box is defined in ISO/IEC 23001-7.

This is an ISO Base Media File Format (MP4) structure used to convey information about the protection system. It’s only necessary with Widevine and PlayReady. If you use those protection systems, you should include a PSSH box for each system you use in the media initialization sections of your stream.

The following is the layout of the version 0 PSSH box.

```swift
PSSH box {
    UInt32 size               // Length of the whole box
    UInt32 type               // == ‘pssh’
    UInt32 version_and_flags  // == 0
    UInt8 SystemID[16]
    UInt32 DataSize
    UInt8 Data[DataSize]      // System specific data
}
```

The `SystemID` is a UUID that indicates how to parse the `Data` portion of the PSSH.

##### Widevine Pssh Data

The Widevine `SystemID` is `edef8ba9-79d6-4ace-a3c8-27dcd51d21ed`.

The `Data` field contains a protocol buﬀer (that is, a mechanism for serializing structured data; see [`Protocol Buffers`](https://developer.apple.comhttps://protobuf.dev)).

The Widevine documentation details the specific messages that are possible.

The data will contain the key identifier and the protection scheme.

##### Playready Pssh Data

The PlayReady `SystemID` is `9a04f079-9840-4286-ab92-e65be0885f95`.

The `Data` field is PlayReady Object that contains a PlayReady Header.

The PlayReady Object is a binary data structure that contains one or more PlayReady Object Records. Each record has a type; one of these types is a PlayReady Header.

The PlayReady Header is a little-endian UTF-16 XML string. This contains the header version, protection scheme, and key identifier. You should use the header version `v4.3.0.0` as this is necessary to support the ‘cbcs’ protection scheme.

#### Example

Here is an example of FairPlay Streaming, Widevine, and PlayReady keys.

```swift
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="skd://test",KEYFORMAT="com.apple.streamingkeydelivery",KEYFORMATVERSIONS="1"
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="data:text/plain;base64,AAAAOHBzc2gAAAAA7e+LqXnWSs6jyCfc1R0h7QAAABgSEAQUJDREVGR0hJSktMTU5PRI88aJmwY=",KEYFORMAT="urn:uuid:edef8ba9-79d6-4ace-a3c8-27dcd51d21ed",KEYFORMATVERSIONS="1"
#EXT-X-KEY:METHOD=SAMPLE-AES,URI="data:text/plain;charset=UTF-16;base64,vgEAAAEAAQC0ATwAVwBSAE0ASABFAEEARABFAFIAIAB4AG0AbABuAHMAPQAiAGgAdAB0AHAAOgAvAC8AcwBjAGgAZQBtAGEAcwAuAG0AaQBjAHIAbwBzAG8AZgB0AC4AYwBvAG0ALwBEAFIATQAvADIAMAAwADcALwAwADMALwBQAGwAYQB5AFIAZQBhAGQAeQBIAGUAYQBkAGUAcgAiACAAdgBlAHIAcwBpAG8AbgA9ACIANAAuADMALgAwAC4AMAAiAD4APABEAEEAVABBAD4APABQAFIATwBUAEUAQwBUAEkATgBGAE8APgA8AEsASQBEAFMAPgA8AEsASQBEACAAQQBMAEcASQBEAD0AIgBBAEUAUwBDAEIAQwAiACAAVgBBAEwAVQBFAD0AIgBOAEMAUQBVAEIARgBSAEUAZABHAFMARQBsAEsAUwAwAHgATgBUAGsAOQBBAD0APQAiAD4APAAvAEsASQBEAD4APAAvAEsASQBEAFMAPgA8AC8AUABSAE8AVABFAEMAVABJAE4ARgBPAD4APAAvAEQAQQBUAEEAPgA8AC8AVwBSAE0ASABFAEEARABFAFIAPgA=",KEYFORMAT="com.microsoft.playready",KEYFORMATVERSIONS="1"
```

##### Fairplay

The FairPlay Streaming URI value, except for the URL scheme prefix, is the key identifier.

##### Widevine

Here is the unpacked form of the Widevine base64 string (a PSSH box).

```None
00000000 00 00 00 38 70 73 73 68 00 00 00 00 ed ef 8b a9 |...8pssh........|
00000010 79 d6 4a ce a3 c8 27 dc d5 1d 21 ed 00 00 00 18 |y.J...'...!.....|
00000020 12 10 04 14 24 34 44 54 64 74 84 94 a4 b4 c4 d4 |....$4DTdt......|
00000030 e4 f4 48 f3 c6 89 9b 06                         |..H.....|
00000038
```

The protocol buﬀer is the last 24 bytes. This buﬀer decodes into two fields: a `key_id` (16 byte value `(04 14 24 34 44 54 64 74 84 94 a4 b4 c4 d4 e4 f4)`, and a `protection_scheme` (a `var-int` that decodes to `63 62 63 73` or `‘cbcs’`). While this example contains only two fields, additional optional fields could be present.

##### Playready

Here is unpacked form of the PlayReady base64 string (a PlayReady Object).

```None
00000000 be 01 00 00 01 00 01 00 b4 01 3c 00 57 00 52 00 |..........<.W.R.|
00000010 4d 00 48 00 45 00 41 00 44 00 45 00 52 00 20 00 |M.H.E.A.D.E.R. .|
00000020 78 00 6d 00 6c 00 6e 00 73 00 3d 00 22 00 68 00 |x.m.l.n.s.=.".h.|
00000030 74 00 74 00 70 00 3a 00 2f 00 2f 00 73 00 63 00 |t.t.p.:././.s.c.|
00000040 68 00 65 00 6d 00 61 00 73 00 2e 00 6d 00 69 00 |h.e.m.a.s...m.i.|
00000050 63 00 72 00 6f 00 73 00 6f 00 66 00 74 00 2e 00 |c.r.o.s.o.f.t...|
00000060 63 00 6f 00 6d 00 2f 00 44 00 52 00 4d 00 2f 00 |c.o.m./.D.R.M./.|
00000070 32 00 30 00 30 00 37 00 2f 00 30 00 33 00 2f 00 |2.0.0.7./.0.3./.|
00000080 50 00 6c 00 61 00 79 00 52 00 65 00 61 00 64 00 |P.l.a.y.R.e.a.d.|
00000090 79 00 48 00 65 00 61 00 64 00 65 00 72 00 22 00 |y.H.e.a.d.e.r.".|
000000a0 20 00 76 00 65 00 72 00 73 00 69 00 6f 00 6e 00 | .v.e.r.s.i.o.n.|
000000b0 3d 00 22 00 34 00 2e 00 33 00 2e 00 30 00 2e 00 |=.".4...3...0...|
000000c0 30 00 22 00 3e 00 3c 00 44 00 41 00 54 00 41 00 |0.".>.<.D.A.T.A.|
000000d0 3e 00 3c 00 50 00 52 00 4f 00 54 00 45 00 43 00 |>.<.P.R.O.T.E.C.|
000000e0 54 00 49 00 4e 00 46 00 4f 00 3e 00 3c 00 4b 00 |T.I.N.F.O.>.<.K.|
000000f0 49 00 44 00 53 00 3e 00 3c 00 4b 00 49 00 44 00 |I.D.S.>.<.K.I.D.|
00000100 20 00 41 00 4c 00 47 00 49 00 44 00 3d 00 22 00 | .A.L.G.I.D.=.".|
00000110 41 00 45 00 53 00 43 00 42 00 43 00 22 00 20 00 |A.E.S.C.B.C.". .|
00000120 56 00 41 00 4c 00 55 00 45 00 3d 00 22 00 4e 00 |V.A.L.U.E.=.".N.|
00000130 43 00 51 00 55 00 42 00 46 00 52 00 45 00 64 00 |C.Q.U.B.F.R.E.d.|
00000140 47 00 53 00 45 00 6c 00 4b 00 53 00 30 00 78 00 |G.S.E.l.K.S.0.x.|
00000150 4e 00 54 00 6b 00 39 00 41 00 3d 00 3d 00 22 00 |N.T.k.9.A.=.=.".|
00000160 3e 00 3c 00 2f 00 4b 00 49 00 44 00 3e 00 3c 00 |>.<./.K.I.D.>.<.|
00000170 2f 00 4b 00 49 00 44 00 53 00 3e 00 3c 00 2f 00 |/.K.I.D.S.>.<./.|
00000180 50 00 52 00 4f 00 54 00 45 00 43 00 54 00 49 00 |P.R.O.T.E.C.T.I.|
00000190 4e 00 46 00 4f 00 3e 00 3c 00 2f 00 44 00 41 00 |N.F.O.>.<./.D.A.|
000001a0 54 00 41 00 3e 00 3c 00 2f 00 57 00 52 00 4d 00 |T.A.>.<./.W.R.M.|
000001b0 48 00 45 00 41 00 44 00 45 00 52 00 3e 00       |H.E.A.D.E.R.>.|
000001be
```

The PlayReady Header is the string below. (Converted from UTF-16 with indentation and line breaks added for clarity.)

```swift
<WRMHEADER xmlns="http://schemas.microsoft.com/DRM/2007/03/PlayReadyHeader" version="4.3.0.0">
    <DATA>
        <PROTECTINFO>
            <KIDS>
                <KID ALGID="AESCBC" VALUE="NCQUBFREdGSElKS0xNTk9A==">
                </KID>
            </KIDS>
        </PROTECTINFO>
    </DATA>
</WRMHEADER>
```

The `ALGID` attribute indicates the protection scheme is ‘cbcs’.

Here is the unpacked form of the `KID` element’s `VALUE` attribute, which is a base64 encoded string.

```None
00000000 34 24 14 04 54 44 74 64 84 94 a4 b4 c4 d4 e4 f4 |4$..TDtd........|
00000010
```

This is a UUID in Microsoft’s GUID form. That is, three little-endian numbers (4 bytes, 2 bytes, 2 bytes) and an eight-byte sequence. In this example the same key identifier is used for PlayReady and Widevine.

## See Also

- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](about-the-common-media-application-format-with-http-live-streaming-hls.md)
  Learn the Common Media Application Format as it applies to HLS.
- [Enabling Low-Latency HTTP Live Streaming (HLS)](enabling-low-latency-http-live-streaming-hls.md)
  Add Low-Latency HLS to your content streams to maintain scalability.
- [Links to additional specifications and videos](links-to-additional-specifications-and-videos.md)
  Review additional specifications and documents.
- [Videos about HLS](videos-about-hls.md)
  Review informational videos about HTTP Live Streaming.
- [Providing metadata for xHE-AAC video soundtracks](providing-metadata-for-xhe-aac-video-soundtracks.md)
  Ensure volume normalization by including metadata for loudness and dynamic range control.
- [Adjusting anchor loudness](adjusting-anchor-loudness.md)
  Adjust anchor loudness when measurements of speech-gated loudness for a full mix may be inaccurate, such as when speech activity is low.
- [Providing JavaScript Object Notation (JSON) chapters](providing-javascript-object-notation-json-chapters.md)
  Prepare JSON chapters for HTTP Live Streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/using-content-protection-systems-with-hls)*