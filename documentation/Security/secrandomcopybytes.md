# SecRandomCopyBytes(_:_:_:)

**Framework**: Security  
**Kind**: func

Generates an array of cryptographically secure random bytes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecRandomCopyBytes(_ rnd: SecRandomRef?, _ count: Int, _ bytes: UnsafeMutableRawPointer) -> Int32
```

#### Return Value

A result code set to [`errSecSuccess`](errsecsuccess.md) or some other value on failure.

#### Discussion

Always test the returned status to make sure that the array has been updated with new, random data before trying to use the values. For example, to create 10 random bytes:

## Parameters

- `rnd`: The random number generator object to use. Specify   to use the default random number generator.
- `count`: The number of random bytes to return in the array pointed to by the   parameter.
- `bytes`: A pointer to an array that the function fills with cryptographically secure random bytes. Use an array that is large enough to hold at least   bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secrandomcopybytes(_:_:_:))*