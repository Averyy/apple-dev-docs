# initWithItems:

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Creates a section with the provided items.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```objc
- (instancetype) initWithItems:(NSArray<id<CPListTemplateItem>> *) items;
```

## Discussion

- Return: An initialized section object.

## Parameters

- `items`: The items to include in the section. CarPlay displays your items in the same order as your array. You can specify only [`CPListItem`](../cplistitem.md), [`CPListImageRowItem`](../cplistimagerowitem.md), and [`CPMessageListItem`](../cpmessagelistitem.md) types in your array. You can’t specify custom types that conform to the [`CPListTemplateItem`](../cplisttemplateitem.md) protocol. If you specify an empty array, the list interface hides the section. Empty sections count against the maximum number of allowed sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/initwithitems:)*