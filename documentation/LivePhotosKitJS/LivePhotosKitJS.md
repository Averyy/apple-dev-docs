# LivePhotosKit JS

**Framework**: Livephotoskitjs  
**Kind**: module

Play Live Photos on the web.

**Availability**:
- LivePhotosKit JS 1.0+

#### Overview

Use the LivePhotosKit JS library to play Live Photos on your web pages.

The JavaScript API presents the player in the form of a DOM element, much like an image or video tag, which can be configured with photo and video resources and other options, and have its playback controlled either programmatically by the consuming developer, or via pre-provided controls by the browsing end-user.

##### Before You Begin

1. Embed LivePhotosKit JS in your webpage.

Use the script tag and link to Apple’s hosted version of LivePhotosKit JS at [`https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js`](https://developer.apple.comhttps://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js)`.`

```javascript
<script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
```

> **Note**:  The LivePhotosKit JS version number is in the URL. For example, 1 specifies LivePhotosKit JS 1.0.0.

1. Enable JavaScript strict mode.

To enable strict mode for an entire script, put ‘use strict’ before any other statements.

```javascript
 'use strict';
```

> **Note**:  LivePhotosKit JS is also available through NPM at [`https://www.npmjs.com/package/livephotoskit`](https://developer.apple.comhttps://www.npmjs.com/package/livephotoskit). The install command is: `npm install --save livephotoskit`

##### Declarative Html

By including the LivePhotosKit JS script on your page, you can create players by simply adding declarative markup to your HTML. As the page loads, LivePhotosKit JS will determine what player instances are on the page and initialize them. You can use any HTML tag that supports child nodes.

At minimum, each tag requires the `data-live-photo` attribute as well as a non-zero height and width. Doing this allows LivePhotosKit JS to find the DOM elements to be initialized as players.

Then you can specify the locations of the photo and video components by setting the `data-photo-src` and `data-video-src` attributes, respectively.

Optionally, you can use the following additional data attributes:

- `data-photo-time`: The timestamp from the beginning of the provided video component, at which the still photo was captured.
- `data-proactively-loads-video`: Whether or not the Player will download the bytes at the provided data-video-src prior to the user or developer attempting to begin playback.
- `data-shows-native-controls`: Whether or not the playback controls are enabled for the user.

Each DOM element assigned to be a Player will be decorated with a playback control.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <script src="https://cdn.apple-livephotoskit.com/lpk/1/livephotoskit.js"></script>
    </head>
    <body>
        <div
            data-live-photo
            data-photo-src="https://..."
            data-video-src="https://..."
            style="width: 320px; height: 320px">            
        </div>
    </body>
</html>
```

##### Javascript Api

Create a new [`LivePhotosKit.Player`](livephotoskit.player/livephotoskit.player.md) by invoking it either as a wrapper around a pre-existing DOM element, or by calling it without an argument, which will create a new DOM element.

```javascript
// A Player built from a new DIV:
const myNewPlayer = LivePhotosKit.Player();
document.body.appendChild(myNewPlayer);
// A Player built from a pre-existing element:
LivePhotosKit.Player(document.getElementById('myExistingElement'));
```

After a Player is created, use the properties and methods to set it up and use it, just as you would with a native image or video element.

The player will emit these events:

- [`canplay`](livephotoskit.player#canplay.md) when the Player has obtained just enough video frames and is obtaining them quickly enough for smooth playback.
- [`error`](livephotoskit.player#error.md) when loading of either the photo or video components of the Live Photo has failed.
- [`ended`](livephotoskit.player#ended.md) when playback of the Live Photo has completed.
- [`videoload`](livephotoskit.player#videoload.md) when the video component of the Live Photo has finished loading.
- [`photoload`](livephotoskit.player#photoload.md) when the photo component of the Live Photo has finished loading.

```javascript
// Create the player using a pre-existing DOM element.
const player = LivePhotosKit.Player(document.getElementById('my-live-photo-target-element'));
player.photoSrc = 'https://...';
player.videoSrc = 'https://...';
// Listen to events the player emits.
player.addEventListener('canplay', evt => console.log('player ready', evt));
player.addEventListener('error', evt => console.log('player load error', evt));
player.addEventListener('ended', evt => console.log('player finished playing through', evt));
// Use the playback controls.
player.playbackStyle = LivePhotosKit.PlaybackStyle.HINT;
player.playbackStyle = LivePhotosKit.PlaybackStyle.FULL;
player.play();
player.pause();
player.toggle();
player.stop();
// Seek the animation to one quarter through.
player.currentTime = 0.25 * player.duration;
// Seek the animation to 0.1 seconds into the Live Photo.
player.currentTime = 0.1;
```

##### Error Handling

A Player will emit error events, if and when errors occur while attempting to load or play. If a Player does experience an error, it will also publish the error to its public property [`errors`](livephotoskit.player/errors.md) as a way to convey whether or not it is in an error state, and, if so, what the errors were.

The error states can be seen here [`LivePhotosKit.Errors`](livephotoskit.errors.md).

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
        // Extract error.
        console.error(ev.detail.error);
    }
})
```

##### Browser Compatibility

The LivePhotosKit JS player is supported on the following browsers:

| Device | Browser |
| --- | --- |
| iOS | Safari, Chrome |
| macOS | Safari, Chrome, Firefox |
| Android (performance depends on device) | Chrome (beta) |
| Windows | Chrome, Firefox, Edge, Internet Explorer 11 |

##### How to Obtain Live Photo Assets

Live Photos consist of two components: a still photo and a video of the moments just before and after the photo is taken. Using one of the following methods will let you obtain the still photo as a JPG and the video as a MOV file.

> ❗ **Important**:  If the assets are large, they will take a long time to download. If the photo takes too long, it will not be able to show the progress badge. To avoid this problem, the element that is being decorated to be a player should explicitly specify its height and width. Downsizing assets will greatly improve performance and reduce bandwidth usage.

A sample project is also [`available`](https://developer.apple.comhttps://developer.apple.com/library/content/samplecode/UsingPhotosFramework/Introduction/Intro.html).

###### Using Macos Photos

- Connect your iOS device to your Mac.
- Import your photos into the Photos application.
- Select the Live Photo you wish to export.
- Use File > Export > Export Unmodified Original to export to your file system.

###### Using Macos Image Capture

- Connect your iOS device to your Mac.
- Select the Live Photo you wish to import from your device to your local file system.
- Choose the destination folder and click on Import.

###### Using Windows 10 File Explorer

- Ensure that iTunes for Windows is installed. You can download it from here: [`http://www.apple.com/itunes/download/`](https://developer.apple.comhttp://www.apple.com/itunes/download/)
- Open File Explorer. This can be opened by pressing the Windows Key and E at the same time.
- Connect your iOS device to your PC.
- You should see your iOS device in the “This PC” folder.
- Navigate to the following folder: (your device) > Internal Storage > DCIM and look for the Live Photo you wish to import.
- Your Live Photo will be stored as a pair of files: a JPG file and a MOV file.
- Drag the pair of files to your local file system.

## Topics

### Classes
- [LivePhotosKit](livephotoskit.md)
  The namespace for the LivePhotosKit library.
- [LivePhotosKit.Player](livephotoskit.player.md)
  A player for Live Photos.
### Enumerations
- [LivePhotosKit.Errors](livephotoskit.errors.md)
  The errors that can occur when playing a LivePhoto.
- [LivePhotosKit.PlaybackStyle](livephotoskit.playbackstyle.md)
  Possible playback styles.
- [LivePhotosKit.EffectType](livephotoskit.effecttype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/LivePhotosKitJS)*