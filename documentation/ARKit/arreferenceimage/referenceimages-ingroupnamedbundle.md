# referenceImages(inGroupNamed:bundle:)

**Framework**: ARKit  
**Kind**: method

Loads all reference images in the specified AR Resource Group in your Xcode project’s asset catalog.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.1+

## Declaration

```swift
class func referenceImages(inGroupNamed name: String, bundle: Bundle?) -> Set<ARReferenceImage>?
```

#### Return Value

A set of all unique reference images in the specified group.

#### Discussion

To use the images for image detection in a world-tracking AR session, provide this set for your session configuration’s [`detectionImages`](arworldtrackingconfiguration/detectionimages.md) property.

## Parameters

- `name`: The name of an AR Resource Group from your Xcode project’s main asset catalog.
- `bundle`: The bundle from which to load asset catalog resources, or   to use your app’s main bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceimage/referenceimages(ingroupnamed:bundle:))*