# NSServicesMenuRequestor

**Framework**: AppKit  
**Kind**: protocol

A set of methods that support interaction with items users can share through a sharing service.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSServicesMenuRequestor : NSObjectProtocol
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Overview

This informal protocol consists of two methods, [`writeSelection(to:types:)`](nsservicesmenurequestor/writeselection(to:types:).md) and [`readSelection(from:)`](nsservicesmenurequestor/readselection(from:).md). The first method provides data to a remote service, and the second receives any data the remote service might send back. Both respond to messages that are generated when the user chooses a command from the Services menu.

## Topics

### Working with Pasteboards
- [func readSelection(from: NSPasteboard) -> Bool](nsservicesmenurequestor/readselection(from:).md)
  Reads data from the pasteboard and uses it to replace the current selection.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nsservicesmenurequestor/writeselection(to:types:).md)
  Writes the current selection to the pasteboard.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSSharingService](nssharingservice.md)
  An object that facilitates the sharing of content with social media services, or with apps like Mail or Safari.
- [class NSSharingServicePicker](nssharingservicepicker.md)
  A list of sharing services that the user can choose from.
- [protocol NSPreviewRepresentableActivityItem](nspreviewrepresentableactivityitem.md)
  An interface you adopt in custom objects that you want to share using the macOS share sheet.
- [class NSSharingServicePickerToolbarItem](nssharingservicepickertoolbaritem.md)
  A toolbar item that displays the macOS share sheet.
- [protocol NSCloudSharingServiceDelegate](nscloudsharingservicedelegate.md)
  A set of methods for responding to the life cycle events of the cloud-sharing service.
- [Services Functions](services-functions.md)
  Configure the contents of your app’s Services menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor)*