# unregisterPersistentChangesObserver(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Unregisters a previously registered persistent changes observer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func unregisterPersistentChangesObserver(_ observer: any PHPhotoLibraryPersistentChangesObserver)
```

```objc
- (void) unregisterPersistentChangesObserver:(id<PHPhotoLibraryPersistentChangesObserver>) observer;
```

## Discussion

After calling this method, the observer will no longer receive persistent changes callbacks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/unregisterpersistentchangesobserver(_:))*