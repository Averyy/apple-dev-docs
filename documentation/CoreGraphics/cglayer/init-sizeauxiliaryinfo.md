# init(_:size:auxiliaryInfo:)

**Framework**: Core Graphics  
**Kind**: init

Creates a layer object that is associated with a graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(_ context: CGContext, size: CGSize, auxiliaryInfo: CFDictionary?)
```

#### Return Value

A CGLayer object. In Objective-C, you’re responsible for releasing this object using the function [`CGLayerRelease`](cglayerrelease.md) when you no longer need the layer.

#### Discussion

After you create a [`CGLayer`](cglayer.md) object, you should reuse it whenever you can to facilitate the Core Graphics caching strategy. Core Graphics caches any objects that are reused, including [`CGLayer`](cglayer.md) objects. Objects that are reused frequently remain in the cache. In contrast, objects that are used once in a while may be moved in and out of the cache according to their frequency of use. If you don’t reuse [`CGLayer`](cglayer.md) objects, Core Graphics won’t cache them. This means that you lose an opportunity to improve the performance of your application.

## Parameters

- `context`: The graphics context you want to create the layer relative to. The layer uses this graphics context as a reference for initialization.
- `size`: The size, in default user space units, of the layer relative to the graphics context.
- `auxiliaryInfo`: Reserved for future use. Pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cglayer/init(_:size:auxiliaryinfo:))*