# init(text:cardElements:allowsMultipleLines:)

**Framework**: CarPlay  
**Kind**: init  
**Role**: Initializer

Initializes the row with the specified text and card-style elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
init(text: String?, cardElements elements: [CPListImageRowItemCardElement], allowsMultipleLines: Bool)
```

```objc
- (instancetype) initWithText:(NSString *) text cardElements:(NSArray<CPListImageRowItemCardElement *> *) elements allowsMultipleLines:(BOOL) allowsMultipleLines;
```

## Return Value

An initialized row with the specified card elements.

## Parameters

- `text`: The text to display above the row. Specify `nil` to omit the text.
- `elements`: The card elements to display. Each element displays its image and text with a background tint color in a playing card shape. Limit the number of items in this parameter to the value in [`CPMaximumNumberOfGridImages`](../cpmaximumnumberofgridimages.md). If your array contains more elements than the maximum, CarPlay doesn’t store references to elements past the maximum number.
- `allowsMultipleLines`: `true` if you allow the row to display multiple lines of elements. Specify `false` to display only one line of elements. If this parameter is `false` and the number of displayable elements don’t fit on one line, CarPlay displays only as many elements as it can and ignores the rest.

## See Also

### Creating a list image row item
- [init(text: String?, elements: [CPListImageRowItemRowElement], allowsMultipleLines: Bool)](./init%28text,elements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and row elements.
- [init(text: String?, condensedElements: [CPListImageRowItemCondensedElement], allowsMultipleLines: Bool)](./init%28text,condensedelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and condensed-height elements.
- [init(text: String?, gridElements: [CPListImageRowItemGridElement], allowsMultipleLines: Bool)](./init%28text,gridelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and grid elements.
- [init(text: String?, imageGridElements: [CPListImageRowItemImageGridElement], allowsMultipleLines: Bool)](./init%28text,imagegridelements,allowsmultiplelines%29.md)
  Initializes the row with the specified text and image grid elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitem/init(text:cardelements:allowsmultiplelines:))*