# NSLogv(_:_:)

**Framework**: Foundation  
**Kind**: func

Logs an error message to the Apple System Log facility.

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
func NSLogv(_ format: String, _ args: CVaListPointer)
```

#### Discussion

Logs an error message to the Apple System Log facility (see `man 3 asl`). If the `STDERR_FILENO` file descriptor has been redirected away from the default or is going to a tty, it will also be written there. If you want to direct output elsewhere, you need to use a custom logging facility.

The message consists of a timestamp and the process ID prefixed to the string you pass in. You compose this string with a format string, `format`, and one or more arguments to be inserted into the string. The format specification allowed by these functions is that which is understood by `NSString`’s formatting capabilities (which is not necessarily the set of format escapes and flags understood by `printf`). The supported format specifiers are described in [`String Format Specifiers`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/formatSpecifiers.html#//apple_ref/doc/uid/TP40004265). A final hard return is added to the error message if one is not present in the format.

In general, you should use the [`NSLog`](nslog.md) function instead of calling this function directly. If you do use this function directly, you must have prepared the variable argument list in the `args` argument by calling the standard C macro `va_start`. Upon completion, you must similarly call the standard C macro `va_end` for this list.

Output from `NSLogv` is serialized, in that only one thread in a process can be doing the writing/logging described above at a time. All attempts at writing/logging a message complete before the next thread can begin its attempts.

The effects of `NSLogv` are not serialized with subsystems other than those discussed above (such as the standard I/O package) and do not produce side effects on those subsystems (such as causing buffered output to be flushed, which may be undesirable).

## See Also

- [func NSLog(String, any CVarArg...)](nslog(_:_:).md)
  Logs an error message to the Apple System Log facility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslogv(_:_:))*