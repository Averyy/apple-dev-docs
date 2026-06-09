# NSGestureRecognizerSuppressesMainMenuActions

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether keyboard shortcuts for menu items are ignored while any gesture recognizer is active.

**Availability**:
- macOS 27.0+ (Beta)



**Type**: boolean

**Default**: `NO`

#### Discussion

Set this key to `YES` if your app uses gesture recognizers in contexts where accidental keyboard shortcuts would interfere with the gesture interaction.

AppKit always suppresses keyboard shortcuts during an exclusive gesture (one that locks input to a single view), so this key is only relevant if your app also triggers gestures that are not exclusive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsgesturerecognizersuppressesmainmenuactions)*