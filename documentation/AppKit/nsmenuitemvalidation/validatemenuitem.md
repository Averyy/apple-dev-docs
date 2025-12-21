# validateMenuItem(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Implemented to override the default action of enabling or disabling a specific menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validateMenuItem(_ menuItem: NSMenuItem) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to enable `menuItem`, [`false`](https://developer.apple.com/documentation/Swift/false) to disable it.

#### Discussion

The object implementing this method must be the target of `menuItem`. You can determine which menu item `menuItem` is by querying it for its tag or action.

The following example disables the menu item associated with the `nextRecord` action method when the selected line in a table view is the last one; conversely, it disables the menu item with `priorRecord` as its action method when the selected row is the first one in the table view. (The `countryOrRegionKeys` array contains names that appear in the table view.)

```objc
- (BOOL)validateMenuItem:(NSMenuItem *)item {
    int row = [tableView selectedRow];
    if ([item action] == @selector(nextRecord) &&
        (row == [countryOrRegionKeys indexOfObject:[countryOrRegionKeys lastObject]])) {
        return NO;
    }
    if ([item action] == @selector(priorRecord) && row == 0) {
        return NO;
    }
    return YES;
}
```

## Parameters

- `menuItem`: An   object that represents the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenuitemvalidation/validatemenuitem(_:))*