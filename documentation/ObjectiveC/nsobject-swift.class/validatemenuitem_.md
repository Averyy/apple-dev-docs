# validateMenuItem:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Implemented to override the default action of enabling or disabling a specific menu item.

**Availability**:
- macOS 10.0+ - Deprecated in 11.0

## Declaration

```objc
- (BOOL) validateMenuItem:(NSMenuItem *) menuItem;
```

#### Return Value

[`YES`](../yes.md) to enable `menuItem`, [`NO`](../no.md) to disable it.

#### Discussion

The object implementing this method must be the target of `menuItem`. You can determine which menu item `menuItem` is by querying it for its tag or action.

The following example disables the menu item associated with the `nextRecord` action method when the selected line in a table view is the last one; conversely, it disables the menu item with `priorRecord` as its action method when the selected row is the first one in the table view. (The `countryKeys` array contains names that appear in the table view.)

```objc
- (BOOL)validateMenuItem:(NSMenuItem *)item {
    int row = [tableView selectedRow];
    if ([item action] == @selector(nextRecord) &&
        (row == [countryKeys indexOfObject:[countryKeys lastObject]])) {
        return NO;
    }
    if ([item action] == @selector(priorRecord) && row == 0) {
        return NO;
    }
    return YES;
}
```

## Parameters

- `menuItem`: An NSMenuItem object that represents the menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/validatemenuitem:)*