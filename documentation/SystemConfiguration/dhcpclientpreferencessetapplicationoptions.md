# DHCPClientPreferencesSetApplicationOptions

**Framework**: System Configuration  
**Kind**: func

Updates the DHCP client preferences to include the specified list of options for the specified application ID.

**Availability**:
- macOS 10.1+

## Declaration

```swift
Boolean DHCPClientPreferencesSetApplicationOptions(CFStringRef applicationID, const UInt8 * options, CFIndex count);
```

#### Return Value

`TRUE` if the operation succeeded; otherwise, `FALSE`.

## Parameters

- `applicationID`: The application’s preference ID (for example, “com.apple.SystemPreferences”).
- `options`: An array of 8-bit values containing the DHCP option codes for the specified application ID (see RFC 2132 for more information on these codes). Pass   to clear the list of options for this application ID.
- `count`: The number of elements in  .

## See Also

- [DHCPClientPreferencesCopyApplicationOptions](dhcpclientpreferencescopyapplicationoptions.md)
  Returns the list of options for the specified application ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpclientpreferencessetapplicationoptions)*