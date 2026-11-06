# init(archiveURL:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Loads a reference object from the specified file URL.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
init(archiveURL url: URL) throws
```

```objc
- (instancetype) initWithArchiveURL:(NSURL *) url error:(NSError **) error;
```

## Return Value

The reference object contained in the file.

## Discussion

To use the object for detection in a world-tracking AR session, add it to the [`detectionObjects`](../arworldtrackingconfiguration/detectionobjects.md) set in your session configuration.

## Parameters

- `url`: The local file URL containing the reference object to load.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/init(archiveurl:))*