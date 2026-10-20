# removeSuite(named:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the specified domain from the search list of the current object.

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
func removeSuite(named suiteName: String)
```

```objc
- (void) removeSuiteNamed:(NSString *) suiteName;
```

## Parameters

- `suiteName`: The bundle identifier for the domain you want to remove. Specify the same string you used when you added the domain.

## See Also

### Adding and removing search domains
- [func addSuite(named: String)](./addsuite%28named%29.md)
  Inserts settings for the specified domain into the search list of the current object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removesuite(named:))*