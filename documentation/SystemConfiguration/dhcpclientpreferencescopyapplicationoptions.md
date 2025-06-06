# DHCPClientPreferencesCopyApplicationOptions

**Framework**: System Configuration  
**Kind**: func

Returns the list of options for the specified application ID.

**Availability**:
- macOS 10.1+

## Declaration

```swift
UInt8 * DHCPClientPreferencesCopyApplicationOptions(CFStringRef applicationID, CFIndex * count);
```

#### Return Value

The list of options for the specified application ID, or `NULL` if no options are defined or if an error occurred. Use free(3) to release a non-`NULL` return value.

## Parameters

- `applicationID`: The application’s preference ID (for example, “com.apple.SystemPreferences”).
- `count`: The number of elements in the list of options.

## See Also

- [DHCPClientPreferencesSetApplicationOptions](dhcpclientpreferencessetapplicationoptions.md)
  Updates the DHCP client preferences to include the specified list of options for the specified application ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/dhcpclientpreferencescopyapplicationoptions)*