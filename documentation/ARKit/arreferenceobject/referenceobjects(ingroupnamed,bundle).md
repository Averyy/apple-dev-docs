# referenceObjects(inGroupNamed:bundle:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

Loads all reference objects in the specified AR Resource Group in your Xcode project’s asset catalog.

**Availability**:
- iOS 12.0+ - Deprecated in 27.0
- iPadOS 12.0+ - Deprecated in 27.0

> **Deprecated**: Only supported for legacy reference objects.

## Declaration

```swift
class func referenceObjects(inGroupNamed name: String, bundle: Bundle?) -> Set<ARReferenceObject>?
```

```objc
+ (NSSet<ARReferenceObject *> *) referenceObjectsInGroupNamed:(NSString *) name bundle:(NSBundle *) bundle;
```

#### Return Value

A set of all unique reference objects in the specified group.

#### Discussion

To use the objects for detection in a world-tracking AR session, provide this set for your session configuration’s [`detectionObjects`](../arworldtrackingconfiguration/detectionobjects.md) property.

## Parameters

- `name`: The name of an AR Resource Group from your Xcode project’s main asset catalog.
- `bundle`: The bundle from which to load asset catalog resources, or `nil` to use your app’s main bundle.

## See Also

### Loading Reference Objects
- [init(archiveURL: URL) throws](./init%28archiveurl%29.md)
  Loads a reference object from the specified file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/referenceobjects(ingroupnamed:bundle:))*