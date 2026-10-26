# reporterForDomain:

**Framework**: StateReporting  
**Kind**: method  
**Role**: Type Method

Returns the reporter instance unique to the given domain name.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
+ (instancetype) reporterForDomain:(NSString *) domain;
```

#### Return Value

The reporter instance for the specified domain.

#### Discussion

This method is the only way to obtain an `SRStateReporter`. Calling it multiple times with the same domain string always returns the same object.

## Parameters

- `domain`: The reverse DNS-style name of the domain whose state you are reporting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/srstatereporter/reporterfordomain:)*