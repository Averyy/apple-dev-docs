# Preparing Audio for HTTP Live Streaming

**Framework**: HTTP Live Streaming

Encode your media properly to ensure synchronized audio and video playback.

#### Overview

Producing media for HTTP Live Streaming (HLS) requires special considerations if you’re encoding audio using the Advanced Audio Coding (AAC) family of formats.

AAC audio processing requires a small amount of leading “throw-away” audio to prime the encoder and initialize internal tables. This small amount of audio results from  which happens during encoding to produce properly formed, encoded audio packets, and its duration is commonly referred to as the . This audio needs to occur before the first frame of video; otherwise, there will be no audio for the first few frames of video.

![Illustration of audio priming samples in the audio track located ahead of the video samples in the video track.](https://docs-assets.developer.apple.com/published/c2ceacf9189804d8b5d286710141f294/preparing-audio-for-http-live-streaming-1%402x.png)

The audio sample rates are normally 44.1 kHz or 48 kHz. For more information, see the [`HTTP Live Streaming Specification`](https://developer.apple.comhttps://tools.ietf.org/html/draft-pantos-hls-rfc8216bis) and the [`HTTP Live Streaming (HLS) authoring specification for Apple devices`](hls-authoring-specification-for-apple-devices.md).

##### Encode Mpeg 2 Transport Stream Segments

MPEG-2 transport streams create an arbitrary timestamp when encoding media, using an 33-bit clock that rolls over every 26 hours. For example, if your video starts at the two-hour mark, your audio starts at two hours plus the time for the leading audio. Therefore, a segment of audio that’s paired with a segment of video starting at the two-hour mark needs audio that starts at the two-hour mark minus the priming duration. This additional segment ensures the first frame of video plays synchronously with the audio.

##### Encode Fragmented Mpeg 4 Segments

The MPEG-4 file format (ISO BMFF) carries the presumption that all track timelines begin with time zero, regardless of whether the timeline is divided into fragments. However, you can set the initial decode time of any fragment to an arbitrary value by means of the Track Fragment Base Media Decode Time Box (`tfdt`). Use this box to permit the alignment of the audio timeline with the video timeline that places the priming audio prior to the first video frame.

Alternatively, starting with iOS 13.1 it’s possible to utilize an Edit List Box (`elst`) within the Track Box (`trak`) in order to place the duration of the priming audio prior to time 0. This permits a natural alignment of other tracks with audio at time 0. The edit list needs to have a single entry in which the value of `media_start` is equivalent to the audio priming duration and the value of `segment_duration` is 0. This is the recommended approach for time alignment for the Common Media Application Format (CMAF).

##### Handle Play Position Changes Within Content

Changing the play position to a specific point in time within content is known as , and is another consideration for encoding audio. HTTP Live Streaming (HLS) has individual segments that are individually downloadable; each contains media data for 4 to 6 seconds of the overall media timeline. When seeking into a point in the video, skip over the intervening segments between the current and target play position and load the appropriate segment.

## See Also

- [Deploying a Basic HTTP Live Streaming (HLS) Stream](deploying-a-basic-http-live-streaming-hls-stream.md)
  Create a basic webpage to deliver HLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/preparing-audio-for-http-live-streaming)*