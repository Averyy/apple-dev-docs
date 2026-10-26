# code

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The code indicating whether your app successfully handled the intent.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSearchForNotebookItemsIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var code: INSearchForNotebookItemsIntentResponseCode { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INSearchForNotebookItemsIntentResponseCode code;
```

*macOS*

```objc
@property (atomic, readonly) INSearchForNotebookItemsIntentResponseCode code;
```

#### Discussion

The value of this property is set automatically at initialization time and cannot be changed later.

## See Also

### Getting the Response Code
- [enum INSearchForNotebookItemsIntentResponseCode](../insearchfornotebookitemsintentresponsecode.md)
  Constants indicating the state of the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchfornotebookitemsintentresponse/code)*