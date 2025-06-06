# NSPrefPaneIconLabel

**Framework**: Bundle Resources  
**Kind**: typealias

The name of a preference pane displayed beneath the preference pane icon in the System Preferences app.

**Availability**:
- macOS 10.0+

#### Discussion

For long names, you can split the name into two lines by including a newline character (`‘\n’`) in the string. If you omit this key, System Preferences uses the [`CFBundleName`](information-property-list/cfbundlename.md) key for the name.

## See Also

- [NSPrefPaneIconFile](information-property-list/nsprefpaneiconfile.md)
  The name of an image file used to represent a preference pane in the System Preferences app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsprefpaneiconlabel)*