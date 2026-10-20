# help()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns information about how to use the commands of the debugger object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func help() -> any UIFocusDebuggerOutput
```

```objc
+ (id<UIFocusDebuggerOutput>) help;
```

#### Discussion

Call this method from the `lldb` debugger using the following commands:

**Swift**:

```swift
po UIFocusDebugger.help()
```

**Objective-C**:

```objc
po [UIFocusDebugger help]
```

The method returns information about how to use the other methods of this class to get information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusdebugger/help())*