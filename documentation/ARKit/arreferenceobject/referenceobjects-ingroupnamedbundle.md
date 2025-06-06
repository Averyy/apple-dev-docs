# referenceObjects(inGroupNamed:bundle:)

**Framework**: ARKit  
**Kind**: method

Loads all reference objects in the specified AR Resource Group in your Xcode project’s asset catalog.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class func referenceObjects(inGroupNamed name: String, bundle: Bundle?) -> Set<ARReferenceObject>?
```

#### Return Value

A set of all unique reference objects in the specified group.

#### Discussion

To use the objects for detection in a world-tracking AR session, provide this set for your session configuration’s [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) property.

## Parameters

- `name`: The name of an AR Resource Group from your Xcode project’s main asset catalog.
- `bundle`: The bundle from which to load asset catalog resources, or   to use your app’s main bundle.

## See Also

- [init(archiveURL: URL) throws](arreferenceobject/init(archiveurl:).md)
  Loads a reference object from the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/referenceobjects(ingroupnamed:bundle:))*