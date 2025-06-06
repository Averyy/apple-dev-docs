# register(defaults:)

**Framework**: Foundation  
**Kind**: method

Adds the contents of the specified dictionary to the registration domain.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func register(defaults registrationDictionary: [String : Any])
```

#### Discussion

If there is no registration domain, one is created using the specified dictionary, and [`registrationDomain`](userdefaults/registrationdomain.md) is added to the end of the search list.

The contents of the registration domain are not written to disk; you need to call this method each time your application starts. You can place a plist file in the application’s Resources directory and call [`register(defaults:)`](userdefaults/register(defaults:).md) with the contents that you read in from that file.

## Parameters

- `registrationDictionary`: The dictionary of keys and values you want to register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/register(defaults:))*