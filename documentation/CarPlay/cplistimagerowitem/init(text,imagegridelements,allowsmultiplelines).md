# init(text:imageGridElements:allowsMultipleLines:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initializes the row with the specified text and image grid elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(text: String?, imageGridElements elements: [CPListImageRowItemImageGridElement], allowsMultipleLines: Bool)
```

```objc
- (instancetype) initWithText:(NSString *) text imageGridElements:(NSArray<CPListImageRowItemImageGridElement *> *) elements allowsMultipleLines:(BOOL) allowsMultipleLines;
```

## Return Value

An initialized row with the specified image grid elements.

## Parameters

- `text`: The text to display above the row. Specify `nil` to omit the text.
- `elements`: The grid elements to display. Each element displays an image and minimal text. Limit the number of items in this parameter to the value in [`CPMaximumNumberOfGridImages`](../cpmaximumnumberofgridimages.md). If your array contains more elements than the maximum, CarPlay doesn’t store references to elements past the maximum number.
- `allowsMultipleLines`: `true` if you allow the row to display multiple lines of elements. Specify `false` to display only one line of elements. If this parameter is `false` and the number of displayable elements don’t fit on one line, CarPlay displays only as many elements as it can and ignores the rest.

## See Also

### Creating a list image row item
- [init(text: String?, elements: [CPListImageRowItemRowElement], allowsMultipleLines: Bool)](./init%28text,elements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and row elements.
- [init(text: String?, cardElements: [CPListImageRowItemCardElement], allowsMultipleLines: Bool)](./init%28text,cardelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and card-style elements.
- [init(text: String?, condensedElements: [CPListImageRowItemCondensedElement], allowsMultipleLines: Bool)](./init%28text,condensedelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and condensed-height elements.
- [init(text: String?, gridElements: [CPListImageRowItemGridElement], allowsMultipleLines: Bool)](./init%28text,gridelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and grid elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:imagegridelements:allowsmultiplelines:))*