# init(frame:options:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns a newly allocated SceneKit view object with the specified frame rectangle and options.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
init(frame: CGRect, options: [String : Any]? = nil)
```

*macOS*

```swift
init(frame: NSRect, options: [String : Any]? = nil)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
- (instancetype) initWithFrame:(CGRect) frame options:(NSDictionary<NSString *,id> *) options;
```

*macOS*

```objc
- (instancetype) initWithFrame:(NSRect) frame options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

An initialized view object, or `nil` if the object couldn’t be created.

## Parameters

- `frame`: The frame rectangle for the view, measured in points and specified in the coordinate system of its superview.
- `options`: Rendering options for the view. See [`SCNView`](../scnview.md).

## See Also

### Initializing a SceneKit View
- [SCNView.Option](./option.md)
  Dictionary keys specifying initialization options, used when initializing a SceneKit view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnview/init(frame:options:))*