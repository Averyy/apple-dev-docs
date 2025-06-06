# LivePhotosKit.Player

**Framework**: LivePhotosKit JS  
**Kind**: class

A player for Live Photos.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
interface LivePhotosKit.Player
```

#### Overview

This class provides a default native control allowing users to play Live Photos.

On a desktop browser, when the user moves the pointer over the native control badge, the video starts playing until the user moves the pointer away from the badge or the video ends. If the user moves the pointer before the video ends, the video stops.

On a mobile device, when the user presses the Live Photo, the video starts playing until the user stops pressing or the video ends.

##### Player Events

During the life cycle of a player, several events are generated.  Adding an event listener to the player allows reaction to these events.

###### Videoload

The player emits a `videoload` event after the video component of the Live Photo has finished loading but before the minimum number of frames necessary for smooth playback are decoded. Under normal circumstances, the `canplay` event is emitted after the `videoload` event. The event handler is then passed an `Event` object. The `Player` reference is accessible from the event’s target member.

```javascript
player.addEventListener('videoload', (ev) => {
    // Handle event.
})
```

###### Photoload

The player emits a `photoload` event when the photo component of the Live Photo has finished loading. The event handler is then passed an `Event` object. The Player reference is accessible from the event’s target member.

```javascript
player.addEventListener('photoload', (ev) => {
    // Handle event.
})
```

###### Canplay

The player emits a `canplay` event when the `Player` has obtained just enough video frames and is obtaining them quickly enough for smooth playback. The event handler is then passed an `Event` object. The Player reference is accessible from the event’s target member.

```javascript
player. addEventListener('canplay', (ev) => {
    // Handle event.
})
```

###### Ended

The player emits an `ended` event when playback of the Live Photo has completed. The event handler is then passed an `Event` object. The Player reference is accessible from the event’s target member.

```javascript
player.addEventListener('ended', (ev) => {
    // Handle event.
})
```

###### Error

The player emits an `error` event when loading of either the photo or video components of the Live Photo has failed. The event handler is then passed an `Event` object, which has a detail member containing error information. If LivePhotosKit JS cannot interpret an internal exception, the `error` member of `detail` will be the exception object. The `Player` reference may be obtained from the event’s target member.

```javascript
player.addEventListener('error', (ev) => {
    if (typeof ev.detail.errorCode === 'number') {
        switch (ev.detail.errorCode) {
        case LivePhotosKit.Errors.IMAGE_FAILED_TO_LOAD:
            // Do something
            break;
        case LivePhotosKit.Errors.VIDEO_FAILED_TO_LOAD:
            // Do something
            break;
        }
    } else {
        // Extract Error object.
        console.error(ev.detail.error);
    }
})
```

## Topics

### Initializers
- [LivePhotosKit.Player](livephotoskit.player/livephotoskit.player.md)
  Creates `LivePhotosKit.Player` objects.
### Instance Properties
- [currentTime](livephotoskit.player/currenttime.md)
  The current time, in seconds, of the play head.
- [duration](livephotoskit.player/duration.md)
  The duration, in seconds, of the entire Live Photo.
- [photoHeight](livephotoskit.player/photoheight.md)
  The height, in pixels, of the photo component.
- [photoTime](livephotoskit.player/phototime.md)
  The nominated time, in seconds, of where the photo component should be within the Live Photo video component.
- [photoWidth](livephotoskit.player/photowidth.md)
  The width, in pixels, of the photo component.
- [canPlay](livephotoskit.player/canplay.md)
  A Boolean value that indicates whether the Player is able to begin playback.
- [errors](livephotoskit.player/errors.md)
  An array of errors that occurred when attempting to load resources.
- [frameTimes](livephotoskit.player/frametimes.md)
  An array of timestamps for each second from the beginning of a Live Photo for which the frames reside in the Live Photo.
- [isPlaying](livephotoskit.player/isplaying.md)
  A Boolean value that indicates whether or not the Player is playing.
- [loadProgress](livephotoskit.player/loadprogress.md)
  A numeric value that indicates the progress of loading the Live Photo.
- [metadataVideoSrc](livephotoskit.player/metadatavideosrc.md)
  A string or array buffer that contains metadata about the properties of a Live Photo.
- [photo](livephotoskit.player/photo.md)
  The renderable, image-bearing DOM element (either an image or a canvas) that the Player consumes to render itself to the screen.
- [photoMimeType](livephotoskit.player/photomimetype.md)
  The MIME type of a photo asset.
- [photoSrc](livephotoskit.player/photosrc.md)
  The source of the photo component of the Live Photo.
- [playbackStyle](livephotoskit.player/playbackstyle.md)
  The style of playback that determines the nature of an animation.
- [proactivelyLoadsVideo](livephotoskit.player/proactivelyloadsvideo.md)
  A boolean value that indicates whether the Player downloads bytes before the user begins playback.
- [renderedTime](livephotoskit.player/renderedtime.md)
  The current timestamp, as a floating-point number of seconds from the beginning of the animation, that is truly displayed on the screen.
- [showsNativeControls](livephotoskit.player/showsnativecontrols.md)
  The value of this property indicates whether the Apple-provided playback controls are enabled for the user.
- [video](livephotoskit.player/video.md)
  The playable `HTMLVideoElement` that the Player consumes to obtain video frame data to render to the screen while animating a Live Photo.
- [videoHeight](livephotoskit.player/videoheight.md)
  The height, in pixels, of the underlying video asset provided to the Player.
- [videoMimeType](livephotoskit.player/videomimetype.md)
  The MIME type of the video asset.
- [videoRotation](livephotoskit.player/videorotation.md)
  The angle that the video is displayed.
- [videoSrc](livephotoskit.player/videosrc.md)
  A reference to the source of the video component of this Live Photo.
- [videoWidth](livephotoskit.player/videowidth.md)
  The width, in pixels, of an underlying video asset provided to the Player.
- [wantsToPlay](livephotoskit.player/wantstoplay.md)
  A boolean that indicates whether the Player has been instructed to play.
- [autoplay](livephotoskit.player/autoplay.md)
- [effectType](livephotoskit.player/effecttype.md)
### Instance Methods
- [beginFinishingPlaybackEarly](livephotoskit.player/beginfinishingplaybackearly.md)
  Clips the duration of the renderer early so that the animation begins to fade back to the photo component earlier than it would ordinarily.
- [pause](livephotoskit.player/pause.md)
  Pauses playback at the current time.
- [play](livephotoskit.player/play.md)
  Starts playback if the player is ready, or resumes playback if the player is paused.
- [stop](livephotoskit.player/stop.md)
  Stops playback and rewinds to the current time of zero.
- [toggle](livephotoskit.player/toggle.md)
  Starts playing the video component of Live Photo if the video is paused, or pauses the video if it is playing.
- [updateSize](livephotoskit.player/updatesize.md)
  Updates the size of the player.

## See Also

- [LivePhotosKit](livephotoskit.md)
  The namespace for the LivePhotosKit library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit.player)*