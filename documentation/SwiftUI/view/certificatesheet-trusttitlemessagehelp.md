# certificateSheet(trust:title:message:help:)

**Framework**: SwiftUI  
**Kind**: method

Displays a certificate sheet using the provided certificate trust.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
@MainActor
@preconcurrency func certificateSheet(trust: Binding<SecTrust?>, title: String? = nil, message: String? = nil, help: URL? = nil) -> some View
```

## Parameters

- `trust`: A binding to a SecTrust reference created with   SecTrustCreateWithCertificates (see <Security/SecTrust.h>)   that determines whether to present the certificate sheet.
- `title`: The title to display. Uses a default title if nil.
- `message`: The message to display. Uses a default message if nil.
- `help`: URL for the “Learn More” button. Uses a default URL if nil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/certificatesheet(trust:title:message:help:))*