# Deploying a Basic HTTP Live Streaming (HLS) Stream

**Framework**: HTTP Live Streaming

Create a basic webpage to deliver HLS.

#### Overview

An HLS stream may either be live or on-demand (VOD). The requirements for deploying an HLS stream are:

- Either an HTML page for browsers or a client app to act as a receiver
- A web server or CDN to act as a host
- A way to encode your source material or live streams as fragmented MPEG-4 media files containing HEVC or H.264 video and AAC or AC-3 audio. Although you can use MP3 audio files or MPEG-2 transport streams for H.264 video, these formats aren’t recommended.

##### Create an Html Page

The easiest way to distribute HLS media is to create a webpage that includes the HTML5 `<video>` tag, using an M3U8 playlist file as the video source. For browsers that don’t support the HTML5 video element, or browsers that don’t support HLS, you can include fallback code between the `<video>` and `</video>` tags. For example, you could fall back to a progressive download movie or a Real Time Streaming Protocol (RTSP) stream using the QuickTime plug-in. See [`Safari HTML5 Audio and Video Guide`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/AudioVideo/Conceptual/Using_HTML5_Audio_Video/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009523) for examples. The following example shows the HTML code for a basic webpage.

```swift
<html>
    <head>
        <title>HTTP Live Streaming Example</title>
    </head>
    <body>
        <video src="http://devimages.apple.com/iphone/samples/bipbop/bipbopall.m3u8" height="300" width="400">
        </video>
    </body>
</html>
```

##### Configure a Web Server

HLS streams can be served from an ordinary web server. Configure your web server and associate the MIME types of the files being served with their file extensions. The following table shows the MIME types for HLS.

| File Extension | MIME Type |
| --- | --- |
| `.m3u8` | `vnd.apple.mpegURL` |
| `.ts` | `video/MP2T` |
| `.mp4` | `video/mp4` |

If your web server is constrained with respect to MIME types, you can serve files ending in `.m3u` with MIME type `audio/mpegURL` for compatibility.

Index files are often long and are frequently redownloaded, but because they’re text files, they can be compressed very efficiently. Reduce server overhead by enabling real-time `gzip` compression of `M3U8` index files. The HTTP Live Streaming client automatically unzips compressed index files.

You might need to shorten time-to-live (TTL) values for M3U8 files to achieve proper caching behavior for downstream web caches. M3U8 files are frequently overwritten during live broadcasts, and the latest version should be downloaded for each request. Check with your content delivery service provider for specific recommendations. For VOD, the index file is static and is downloaded only once, so caching isn’t a factor.

##### Validate Your Streams

The `mediastreamvalidator` tool is a command-line utility for validating HLS streams and servers. See [`Using Apple’s HTTP Live Streaming (HLS) Tools`](using-apple-s-http-live-streaming-hls-tools.md) for details on obtaining the tool.

The media stream validator simulates an HLS session and verifies that the index file and media segments conform to the HLS specification. It performs several checks to ensure reliable streaming. If any errors or problems are found, a detailed diagnostic report is displayed. Always run the validator prior to serving a new stream or alternate stream set.

See [`FairPlay Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming/fps/) for details on validating with secure protocols.

##### Serve Key Files Securely Over Https

Protect your media by encrypting it. The file segmenter and stream segmenter tools both have encryption options, and you can configure them to change the encryption key periodically. Who you share the keys with is up to you.

Key files require an initialization vector to decode encrypted media. The initialization vectors can be changed periodically, just as the keys can. The current recommendation for encrypting media while minimizing overhead is to change the key every 3 to 4 hours and change the initialization vector after every 50 Mb of data.

Even with restricted access to keys, it’s possible for an eavesdropper to obtain copies of the key files if they’re sent over HTTP. One solution to this problem is to send the keys securely over HTTPS. Before attempting to serve key files over HTTPS, test serving the keys from an internal web server over HTTP. This allows you to debug your setup before adding HTTPS to the mix. Once you have a known working system, you can make the switch to HTTPS.

The requirements for using HTTPS to serve keys for HLS are:

- Verify that you have an SSL certificate signed by a trusted authority on your HTTPS server. If not, you can still test your setup by creating a self-signed SSL Certificate Authority and a leaf certificate for your server. Attach the certificate for the certificate authority to an email, send it to a device you want to use as an HLS client, and tap the attachment in Mail to make the device trust the server.
- Ensure that the authentication domain for the key files is the same as the authentication domain for the first playlist file. The simplest way to accomplish this is to serve the Multivariant Playlist file from the HTTPS server. The playlist file is downloaded once, so this shouldn’t cause an excessive burden. Other playlist files can be served using HTTP.
- Either initiate your own dialog for the user to authenticate, or store the credentials on the client device. HLS doesn’t provide user dialogs for authentication. If you’re writing your own client app, you can store cookie-based or HTTP credentials and supply them in the [`connection(_:didReceive:)`](https://developer.apple.com/documentation/foundation/nsurlconnectiondelegate/1417135-connection) callback. The credentials you supply are cached and reused by the media player.

A sample-level encryption format is documented in [`MPEG-2 Stream Encryption Format for HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/library/content/documentation/AudioVideo/Conceptual/HLS_Sample_Encryption/Intro/Intro.html#//apple_ref/doc/uid/TP40012862). For the strongest level of content protection, an alternative to serving keys directly over HTTPS is to use FairPlay Streaming. See [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md) for more information.

## See Also

- [Preparing Audio for HTTP Live Streaming](preparing-audio-for-http-live-streaming.md)
  Encode your media properly to ensure synchronized audio and video playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/deploying-a-basic-http-live-streaming-hls-stream)*