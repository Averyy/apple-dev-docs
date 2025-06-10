# init(string:extrusionDepth:)

**Framework**: SceneKit  
**Kind**: init

Creates a text geometry from a specified string, extruded with a specified depth.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(string: Any?, extrusionDepth: CGFloat)
```

#### Return Value

A new text geometry.

#### Discussion

In the local coordinate system of the text geometry, the origin corresponds to the lower left corner of the text’s layout rectangle, with the text extending in the x- and y-axis dimensions. (SceneKit computes a layout rectangle automatically, or you can specify one using the [`containerFrame`](scntext/containerframe.md) property.) The geometry is centered along its z-axis. For example, if its [`extrusionDepth`](scntext/extrusiondepth.md) property is `1.0`, the geometry extends from `-0.5` to `0.5` along the z-axis. An extrusion depth of zero creates a flat, one-sided shape—the geometry is confined to the plane whose z-coordinate is `0.0`, and viewable only from its front unless its material’s [`isDoubleSided`](scnmaterial/isdoublesided.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `string`: An   or   object containing text from which to create the geometry.
- `extrusionDepth`: The extent of the text geometry in the Z dimension of its local coordinate space. Specify a depth of   to create 2D text confined to a plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/init(string:extrusiondepth:))*