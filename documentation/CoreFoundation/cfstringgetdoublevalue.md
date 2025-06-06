# CFStringGetDoubleValue(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the primary `double` value represented by a string.

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
func CFStringGetDoubleValue(_ str: CFString!) -> Double
```

#### Return Value

The `double` value represented by `str`, or `0.0` if there is a scanning error (if the string contains disallowed characters or does not represent a double value).

#### Discussion

Consider the following example:

```objc
double val = CFStringGetDoubleValue(CFSTR("0.123"));
```

The variable `val` in this example would contain the value `0.123` after the function is called.

## Parameters

- `str`: A string that represents a double value. The only allowed characters are the ASCII digit characters (ASCII   -  ), the plus sign (ASCII  ), the minus sign (ASCII  ), and the period character (ASCII  ).

## See Also

- [func CFStringGetIntValue(CFString!) -> Int32](cfstringgetintvalue(_:).md)
  Returns the integer value represented by a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstringgetdoublevalue(_:))*