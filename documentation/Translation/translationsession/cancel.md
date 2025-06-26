# cancel()

**Framework**: Translation  
**Kind**: method

Attempts to stop all ongoing work for the translation session.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
func cancel()
```

#### Discussion

Future requests will throw an error that the session is already cancelled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/cancel())*