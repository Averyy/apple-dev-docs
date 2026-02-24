# MacOSServerAccount.ConfiguredAccountsItem

**Framework**: Device Management  
**Kind**: dictionary

An array of dictionaries containing configured account types and relevant settings

**Availability**:
- iOS 9.0+
- iPadOS 9.0+

## Declaration

```swift
object MacOSServerAccount.ConfiguredAccountsItem
```

## Properties

- `Port` (integer): Designates the port number to use when contacting the server. If no port number is specified, the default port is used.
- `Type` (string) *(required)*: com.apple.osxserver.documents (the Documents account type).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/macosserveraccount/configuredaccountsitem)*