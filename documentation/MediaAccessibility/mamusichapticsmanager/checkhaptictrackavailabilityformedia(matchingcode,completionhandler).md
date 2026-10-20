# checkHapticTrackAvailabilityForMedia(matchingCode:completionHandler:)

**Framework**: Media Accessibility  
**Kind**: method  
**Role**: Instance Method

Checks whether a haptic track is available for the song with the specified International Standard Recording Code (ISRC).

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func checkHapticTrackAvailabilityForMedia(matchingCode internationalStandardRecordingCode: String, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func isHapticTrackAvailable(forMediaMatching internationalStandardRecordingCode: String) async -> Bool
```

```objc
- (void) checkHapticTrackAvailabilityForMediaMatchingCode:(NSString *) internationalStandardRecordingCode completionHandler:(void (^)(BOOL musicHapticsAvailable)) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaaccessibility/mamusichapticsmanager/checkhaptictrackavailabilityformedia(matchingcode:completionhandler:))*