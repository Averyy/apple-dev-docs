# init(strokes:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a drawing object with the strokes you supply.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(strokes: [PKStroke])
```

```objc
- (instancetype) initWithStrokes:(NSArray<PKStroke *> *) strokes;
```

## Parameters

- `strokes`: An array of [`PKStrokeReference`](../pkstrokereference.md) elements.

## See Also

### Creating a drawing object
- [init(data: Data) throws](./init%28data%29.md)
  Creates a drawing object and populates it with previously drawn content.
- [init()](./init%28%29.md)
  Creates an empty drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/init(strokes:))*