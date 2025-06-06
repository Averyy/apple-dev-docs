# CFStringGetIntValue(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the integer value represented by a string.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFStringGetIntValue(_ str: CFString!) -> Int32
```

#### Return Value

The signed integer value represented by `str`. The result is `0` if there is a scanning error (if the string contains disallowed characters or does not represent an integer value) or `INT_MAX` or `INT_MIN` if there is an overflow error.

#### Discussion

Consider the following example:

```objc
SInt32 val = CFStringGetIntValue(CFSTR("-123"));
```

The variable `val` in this example would contain the value `-123` after the function is called.

## Parameters

- `str`: A string that represents a signed integer value. The only allowed characters are the ASCII digit characters (ASCII   -  ), the plus sign (ASCII  ), the minus sign (ASCII  ), and the period character (ASCII  ).

## See Also

- [func CFStringGetDoubleValue(CFString!) -> Double](cfstringgetdoublevalue(_:).md)
  Returns the primary `double` value represented by a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetintvalue(_:))*