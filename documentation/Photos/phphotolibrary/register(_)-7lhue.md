# register(_:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Registers an observer to be notified when persistent changes occur in the photo library.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func register(_ observer: any PHPhotoLibraryPersistentChangesObserver)
```

```objc
- (void) registerPersistentChangesObserver:(id<PHPhotoLibraryPersistentChangesObserver>) observer;
```

#### Discussion

The observer is held weakly by the photo library. The observer’s [`photoLibraryPersistentChangesDidUpdate(_:)`](../phphotolibrarypersistentchangesobserver/photolibrarypersistentchangesdidupdate%28_%29.md) method is called on an arbitrary serial queue when changes are committed to the photo library. Use [`fetchPersistentChanges(since:)`](./fetchpersistentchanges%28since%29.md) to retrieve the specific changes.

Requires read-write photo library authorization ([`PHAccessLevel.readWrite`](../phaccesslevel/readwrite.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/register(_:)-7lhue)*