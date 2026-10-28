# init(data:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a drawing object and populates it with previously drawn content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(data: Data) throws
```

```objc
- (instancetype) initWithData:(NSData *) data error:(NSError **) error;
```

## Return Value

A new canvas object initialized with the specified data.

## Parameters

- `data`: The initial data to add to the canvas. Only specify data you previously obtained from a canvas view.

## See Also

### Creating a drawing object
- [convenience init(strokes: [PKStroke])](./init%28strokes%29.md)
  Creates a drawing object with the strokes you supply.
- [init()](./init%28%29.md)
  Creates an empty drawing object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/init(data:))*