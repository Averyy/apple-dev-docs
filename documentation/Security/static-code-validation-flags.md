# Static Code Validation Flags

**Framework**: Security

Use these supplemental flags to test the validity of a static code signature.

#### Overview

These flags supplement the flags described in [`SecCSFlags`](seccsflags.md). Use these additional constants with the flags parameter of the [`SecStaticCodeCheckValidity(_:_:_:)`](secstaticcodecheckvalidity(_:_:_:).md) and [`SecStaticCodeCheckValidityWithErrors(_:_:_:_:)`](secstaticcodecheckvaliditywitherrors(_:_:_:_:).md) functions to control the validation of code in the file system.

## Topics

### Constants
- [var kSecCSCheckAllArchitectures: UInt32](kseccscheckallarchitectures.md)
  For multi-architecture (universal) Mach-O programs, validate all architectures included.
- [var kSecCSDoNotValidateExecutable: UInt32](kseccsdonotvalidateexecutable.md)
  Do not validate the contents of the main executable.
- [var kSecCSDoNotValidateResources: UInt32](kseccsdonotvalidateresources.md)
  Do not validate the presence and contents of all bundle resources (if any).
- [var kSecCSBasicValidateOnly: UInt32](kseccsbasicvalidateonly.md)
  Do not validate either the main executable or the bundle resources, if any.
- [var kSecCSCheckNestedCode: UInt32](kseccschecknestedcode.md)
  For code in bundle form, locate and recursively check embedded code.
- [var kSecCSStrictValidate: UInt32](kseccsstrictvalidate.md)
  Perform additional checks to ensure the validity of code in bundle form.
- [var kSecCSFullReport: UInt32](kseccsfullreport.md)
- [var kSecCSCheckGatekeeperArchitectures: UInt32](kseccscheckgatekeeperarchitectures.md)
- [var kSecCSRestrictSymlinks: UInt32](kseccsrestrictsymlinks.md)
- [var kSecCSRestrictToAppLike: UInt32](kseccsrestricttoapplike.md)
- [var kSecCSRestrictSidebandData: UInt32](kseccsrestrictsidebanddata.md)
- [var kSecCSUseSoftwareSigningCert: UInt32](kseccsusesoftwaresigningcert.md)
- [var kSecCSValidatePEH: UInt32](kseccsvalidatepeh.md)
- [var kSecCSSingleThreaded: UInt32](kseccssinglethreaded.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/static-code-validation-flags)*