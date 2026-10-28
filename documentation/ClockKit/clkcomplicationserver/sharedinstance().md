# sharedInstance()

**Framework**: ClockKit  
**Kind**: method  
**Role**: Type Method

Returns the shared complication server.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
class func sharedInstance() -> Self
```

```objc
+ (instancetype) sharedInstance;
```

## Discussion

Always use this method to retrieve the shared complication server object. Don’t try to create instances of the object yourself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkcomplicationserver/sharedinstance())*