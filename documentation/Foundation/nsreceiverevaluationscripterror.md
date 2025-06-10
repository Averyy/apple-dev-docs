# NSReceiverEvaluationScriptError

**Framework**: Foundation  
**Kind**: var

The object or objects specified by the direct parameter to a command could not be found.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var NSReceiverEvaluationScriptError: Int { get }
```

## See Also

- [var NSNoScriptError: Int](nsnoscripterror.md)
  No error.
- [var NSKeySpecifierEvaluationScriptError: Int](nskeyspecifierevaluationscripterror.md)
  The object or objects specified by a key (for commands that support key specifiers) could not be found.
- [var NSArgumentEvaluationScriptError: Int](nsargumentevaluationscripterror.md)
  The object specified by an argument could not be found.
- [var NSReceiversCantHandleCommandScriptError: Int](nsreceiverscanthandlecommandscripterror.md)
  The receivers don’t support the command sent to them.
- [var NSRequiredArgumentsMissingScriptError: Int](nsrequiredargumentsmissingscripterror.md)
  An argument (or more than one argument) is missing.
- [var NSArgumentsWrongScriptError: Int](nsargumentswrongscripterror.md)
  An argument (or more than one argument) is of the wrong type or is otherwise invalid.
- [var NSUnknownKeyScriptError: Int](nsunknownkeyscripterror.md)
  An unidentified error occurred; indicates an error in the scripting support of your application.
- [var NSInternalScriptError: Int](nsinternalscripterror.md)
  An unidentified internal error occurred; indicates an error in the scripting support of your application.
- [var NSOperationNotSupportedForKeyScriptError: Int](nsoperationnotsupportedforkeyscripterror.md)
  The implementation of a scripting command signaled an error.
- [var NSCannotCreateScriptCommandError: Int](nscannotcreatescriptcommanderror.md)
  Could not create the script command; an invalid or unrecognized Apple event was received.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsreceiverevaluationscripterror)*