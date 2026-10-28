# showPicker(for:completionHandler:)

**Framework**: AccessorySetupKit  
**Kind**: method  
**Role**: Instance Method

Present a picker that shows discovered accessories matching an array of display items.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
func showPicker(for displayItems: [ASPickerDisplayItem], completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func showPicker(for displayItems: [ASPickerDisplayItem]) async throws
```

```objc
- (void) showPickerForDisplayItems:(NSArray<ASPickerDisplayItem *> *) displayItems completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Mentions

- [Discovering and configuring accessories](../discovering-and-configuring-accessories.md)

## Discussion

The session’s event handler receives events when this picker displays and dismisses, as well as when the person using the app picks an accessory.

To migrate previously-configured accessories to AccessorySetupKit, add instances of [`ASMigrationDisplayItem`](../asmigrationdisplayitem.md) to the `displayItems` array.

## Parameters

- `displayItems`: An array of [`ASPickerDisplayItem`](../aspickerdisplayitem.md) instances describing accessories your app can set up. The picker displays only discovered accessories that match the properties of items in this array.
- `completionHandler`: A block or closure that the picker calls when it completes the operation. The completion handler receives an [`NSError`](../../Foundation/nserror.md) instance if the picker encounters an error.

## See Also

### Displaying an accessory picker
- [func showPicker(completionHandler: ((any Error)?) -> Void)](./showpicker%28completionhandler%29.md)
  Present a picker that shows accessories managed by a Device Discovery Extension in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysession/showpicker(for:completionhandler:))*