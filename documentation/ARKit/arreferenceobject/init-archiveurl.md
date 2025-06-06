# init(archiveURL:)

**Framework**: ARKit  
**Kind**: init

Loads a reference object from the specified file URL.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init(archiveURL url: URL) throws
```

#### Return Value

The reference object contained in the file.

#### Discussion

To use the object for detection in a world-tracking AR session, add it to the [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) set in your session configuration.

## Parameters

- `url`: The local file URL containing the reference object to load.

## See Also

- [class func referenceObjects(inGroupNamed: String, bundle: Bundle?) -> Set<ARReferenceObject>?](arreferenceobject/referenceobjects(ingroupnamed:bundle:).md)
  Loads all reference objects in the specified AR Resource Group in your Xcode project’s asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/init(archiveurl:))*