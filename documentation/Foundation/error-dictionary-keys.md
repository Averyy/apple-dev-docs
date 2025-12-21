# Error Dictionary Keys

**Framework**: Foundation

If the result of [`init(contentsOf:error:)`](nsapplescript/init(contentsof:error:).md), [`compileAndReturnError(_:)`](nsapplescript/compileandreturnerror(_:).md), [`executeAndReturnError(_:)`](nsapplescript/executeandreturnerror(_:).md), or [`executeAppleEvent(_:error:)`](nsapplescript/executeappleevent(_:error:).md), signals failure (`nil`, [`false`](https://developer.apple.com/documentation/Swift/false), `nil`, or `nil`, respectively), a pointer to an autoreleased dictionary is put at the location pointed to by the error parameter. The error info dictionary may contain entries that use any combination of the following keys, including no entries at all.

## Topics

### Constants
- [class let errorMessage: String](nsapplescript/errormessage.md)
  An `NSString` that supplies a detailed description of the error condition.
- [class let errorNumber: String](nsapplescript/errornumber.md)
  An `NSNumber` that specifies the error number.
- [class let errorAppName: String](nsapplescript/errorappname.md)
  An `NSString` that specifies the name of the application that generated the error.
- [class let errorBriefMessage: String](nsapplescript/errorbriefmessage.md)
  An `NSString` that provides a brief description of the error.
- [class let errorRange: String](nsapplescript/errorrange.md)
  An `NSValue` that specifies a range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/error-dictionary-keys)*