# init(types:)

**Framework**: Foundation  
**Kind**: init

Initializes and returns a data detector instance.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(types checkingTypes: NSTextCheckingTypes) throws
```

#### Return Value

Returns the newly initialized data detector. If an error was encountered returns `nil`, and `error` contains the error.

#### Discussion

Currently, the supported data detectors `checkingTypes` are:  [`date`](nstextcheckingresult/checkingtype/date.md), [`address`](nstextcheckingresult/checkingtype/address.md), [`link`](nstextcheckingresult/checkingtype/link.md), `NSTextCheckingTypePhoneNumber`, and `NSTextCheckingTypeTransitInformation`.

> **Note**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `checkingTypes`: The checking types. The supported checking types are a subset of the types  . Those constants can be combined using the C-bitwise OR operator.

## See Also

- [var checkingTypes: NSTextCheckingTypes](nsdatadetector/checkingtypes.md)
  Returns the checking types for the data detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdatadetector/init(types:))*