# presentLimitedLibraryPicker(from:)

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method

Prompts the user to update their limited library selection.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func presentLimitedLibraryPicker(from controller: UIViewController)
```

```objc
- (void) presentLimitedLibraryPickerFromViewController:(UIViewController *) controller;
```

#### Discussion

If the user enabled limited library access using [`requestAuthorization(for:handler:)`](./requestauthorization%28for,handler%29.md), use this method to present the limited library picker so they can update their selection. If the user hasn’t enabled limited library access mode for your app, calling this method does nothing. Use this method when disabling the automatic limited library alert prompt. By default, the system automatically prompts the user to update their limited library selection once per app life cycle. To suppress the prompt, add `PHPhotoLibraryPreventAutomaticLimitedAccessAlert` to your app’s `Info.plist` file.

Any changes the user applies to the limited library selection trigger a [`PHPhotoLibraryChangeObserver`](../phphotolibrarychangeobserver.md) update.

## Parameters

- `controller`: The view controller from which to present the limited library picker.

## See Also

### Presenting the Limited Library Picker
- [func presentLimitedLibraryPicker(from: UIViewController, completionHandler: ([String]) -> Void)](./presentlimitedlibrarypicker%28from,completionhandler%29.md)
  Prompts the user to update their limited library selection with a callback providing newly selected identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phphotolibrary/presentlimitedlibrarypicker(from:))*