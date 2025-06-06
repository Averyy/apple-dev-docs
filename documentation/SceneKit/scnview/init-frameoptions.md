# init(frame:options:)

**Framework**: SceneKit  
**Kind**: init

Initializes and returns a newly allocated SceneKit view object with the specified frame rectangle and options.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
init(frame: NSRect, options: [String : Any]? = nil)
```

#### Return Value

An initialized view object, or `nil` if the object couldn’t be created.

## Parameters

- `frame`: The frame rectangle for the view, measured in points and specified in the coordinate system of its superview.
- `options`: Rendering options for the view. See  .

## See Also

- [SCNView.Option](scnview/option.md)
  Dictionary keys specifying initialization options, used when initializing a SceneKit view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/init(frame:options:))*