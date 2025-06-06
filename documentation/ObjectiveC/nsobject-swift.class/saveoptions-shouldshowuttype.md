# saveOptions(_:shouldShowUTType:)

**Framework**: Objective-C Runtime  
**Kind**: method

Called to determine if the specified uniform type identifier should be shown in the save panel.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func saveOptions(_ saveOptions: IKSaveOptions!, shouldShowUTType utType: String!) -> Bool
```

#### Return Value

[`YES`](yes.md) if the specified type should be shown in the save options, otherwise [`NO`](no.md).

## Parameters

- `saveOptions`: The   instance that called the delegate.
- `utType`: The uniform type identifier to test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/saveoptions(_:shouldshowuttype:))*