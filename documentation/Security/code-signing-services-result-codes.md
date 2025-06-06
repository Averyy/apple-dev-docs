# Code Signing Services Result Codes

**Framework**: Security

Recognize result codes specific to the code signing services API.

#### Discussion

Use the [`SecCopyErrorMessageString(_:_:)`](seccopyerrormessagestring(_:_:).md) function to obtain a human readable string corresponding to these status codes.

The functions of the [`Code Signing Services`](code-signing-services.md) API may also return the general codes listed in [`Security Framework Result Codes`](security-framework-result-codes.md). In particular, you might expect to encounter [`errSecSuccess`](errsecsuccess.md), [`errSecUnimplemented`](errsecunimplemented.md), [`errSecParam`](errsecparam.md), and [`errSecAllocate`](errsecallocate.md).

## Topics

### Code-signing format result codes
- [var errSecCSAmbiguousBundleFormat: OSStatus](errseccsambiguousbundleformat.md)
  The bundle could be an app or a framework.
- [var errSecCSBadBundleFormat: OSStatus](errseccsbadbundleformat.md)
  The bundle format is unrecognized, invalid, or unsuitable.
- [var errSecCSBadDictionaryFormat: OSStatus](errseccsbaddictionaryformat.md)
  A required information property list (Info.plist) file or resource is malformed.
- [var errSecCSBadDiskImageFormat: OSStatus](errseccsbaddiskimageformat.md)
  The disk image format unrecognized, invalid, or unsuitable.
- [var errSecCSBadObjectFormat: OSStatus](errseccsbadobjectformat.md)
  The object file format invalid or unsuitable.
### Code-signing database issue result codes
- [var errSecCSDBAccess: OSStatus](errseccsdbaccess.md)
  Cannot access signature database.
- [var errSecCSDBDenied: OSStatus](errseccsdbdenied.md)
  Access to signature database denied.
- [var errSecCSDbCorrupt: OSStatus](errseccsdbcorrupt.md)
  A system database or file is corrupt.
- [var errSecCSSigDBAccess: OSStatus](errseccssigdbaccess.md)
  Can’t access signature database.
- [var errSecCSSigDBDenied: OSStatus](errseccssigdbdenied.md)
  Access to signature database denied.
### Code-signing host protocol issue result codes
- [var errSecCSHostProtocolContradiction: OSStatus](errseccshostprotocolcontradiction.md)
  Host protocol violation: contradictory hosting modes.
- [var errSecCSHostProtocolDedicationError: OSStatus](errseccshostprotocoldedicationerror.md)
  Host protocol violation: operation not allowed with or for a dedicated guest.
- [var errSecCSHostProtocolInvalidAttribute: OSStatus](errseccshostprotocolinvalidattribute.md)
  Code signing host returned invalid or inconsistent attributes for guest code.
- [var errSecCSHostProtocolInvalidHash: OSStatus](errseccshostprotocolinvalidhash.md)
  Host protocol violation: invalid hash of guest code.
- [var errSecCSHostProtocolNotProxy: OSStatus](errseccshostprotocolnotproxy.md)
  Host protocol violation: proxy hosting not engaged.
- [var errSecCSHostProtocolRelativePath: OSStatus](errseccshostprotocolrelativepath.md)
  Host protocol violation: absolute guest path required.
- [var errSecCSHostProtocolStateError: OSStatus](errseccshostprotocolstateerror.md)
  Host protocol violation: invalid guest state change request.
- [var errSecCSHostProtocolUnrelated: OSStatus](errseccshostprotocolunrelated.md)
  Host protocol violation: the specified code is not a guest of the specified code signing host.
### Code-signing signature issue result codes
- [var errSecCSSignatureFailed: OSStatus](errseccssignaturefailed.md)
  Code or signature modified.
- [var errSecCSSignatureInvalid: OSStatus](errseccssignatureinvalid.md)
  Invalid format for signature.
- [var errSecCSSignatureNotVerifiable: OSStatus](errseccssignaturenotverifiable.md)
  Signature cannot be read.
- [var errSecCSSignatureUnsupported: OSStatus](errseccssignatureunsupported.md)
  Unsupported type or version of signature.
- [var errSecCSUnsigned: OSStatus](errseccsunsigned.md)
  Code object is not signed.
- [var errSecCSUnsignedNestedCode: OSStatus](errseccsunsignednestedcode.md)
  Nested code is unsigned.
- [var errSecCSUnsupportedDigestAlgorithm: OSStatus](errseccsunsupporteddigestalgorithm.md)
  The signature digest algorithm(s) specified are not supported.
- [var errSecCSSignatureUntrusted: OSStatus](errseccssignatureuntrusted.md)
  The signature is valid but signer isn’t trusted.
### Code-signing file format issue result codes
- [var errSecCSDSStoreSymlink: OSStatus](errseccsdsstoresymlink.md)
  A `.DS_Store` file can’t be a symlink.
- [var errSecCSFileHardQuarantined: OSStatus](errseccsfilehardquarantined.md)
  File open or execution not allowed.
- [var errSecCSInvalidSymlink: OSStatus](errseccsinvalidsymlink.md)
  Invalid destination for symbolic link in bundle.
- [var errSecCSNoMainExecutable: OSStatus](errseccsnomainexecutable.md)
  The code has no main executable file.
- [var errSecCSRegularFile: OSStatus](errseccsregularfile.md)
  The main executable or Info.plist must be a regular file (and not, for example, a symbolic link).
- [var errSecCSUnsealedAppRoot: OSStatus](errseccsunsealedapproot.md)
  Unsealed contents present in the bundle root.
- [var errSecCSUnsealedFrameworkRoot: OSStatus](errseccsunsealedframeworkroot.md)
  Unsealed contents present in the root directory of an embedded framework.
### Code-signing resource issue result codes
- [var errSecCSResourceDirectoryFailed: OSStatus](errseccsresourcedirectoryfailed.md)
  A directory or its signature has been modified and is therefore invalid.
- [var errSecCSResourceNotSupported: OSStatus](errseccsresourcenotsupported.md)
  Found an unsupported resource.
- [var errSecCSResourceRulesInvalid: OSStatus](errseccsresourcerulesinvalid.md)
  Invalid resource selection rule or rules.
- [var errSecCSResourcesInvalid: OSStatus](errseccsresourcesinvalid.md)
  The sealed resource directory is invalid.
- [var errSecCSResourcesNotFound: OSStatus](errseccsresourcesnotfound.md)
  Cannot find sealed resources in code.
- [var errSecCSResourcesNotSealed: OSStatus](errseccsresourcesnotsealed.md)
  Resources are not sealed by the signature.
### Other result codes
- [var errSecCSBadCallbackValue: OSStatus](errseccsbadcallbackvalue.md)
  The monitor callback returned invalid value.
- [var errSecCSBadFrameworkVersion: OSStatus](errseccsbadframeworkversion.md)
  The embedded framework contains a modified or invalid version.
- [var errSecCSBadLVArch: OSStatus](errseccsbadlvarch.md)
  The library validation flag cannot be used with an i386 binary.
- [var errSecCSBadMainExecutable: OSStatus](errseccsbadmainexecutable.md)
  The main executable failed strict validation.
- [var errSecCSBadNestedCode: OSStatus](errseccsbadnestedcode.md)
  The nested code is modified or invalid.
- [var errSecCSBadResource: OSStatus](errseccsbadresource.md)
  A sealed resource is missing or invalid.
- [var errSecCSCMSTooLarge: OSStatus](errseccscmstoolarge.md)
  The signature is too large to embed.
- [var errSecCSCancelled: OSStatus](errseccscancelled.md)
  The operation was terminated by explicit cancellation.
- [var errSecCSGuestInvalid: OSStatus](errseccsguestinvalid.md)
  The identity of guest code has been invalidated.
- [var errSecCSHelperFailed: OSStatus](errseccshelperfailed.md)
  The codesign_allocate helper tool can’t be found or used.
- [var errSecCSHostReject: OSStatus](errseccshostreject.md)
  Code rejected its host.
- [var errSecCSInfoPlistFailed: OSStatus](errseccsinfoplistfailed.md)
  The Info.plist file or the signature has been modified.
- [var errSecCSInternalError: OSStatus](errseccsinternalerror.md)
  Internal error in Code Signing Services subsystem.
- [var errSecCSInvalidAttributeValues: OSStatus](errseccsinvalidattributevalues.md)
  An attribute value associated with a key is out of range or is the wrong type.
- [var errSecCSInvalidFlags: OSStatus](errseccsinvalidflags.md)
  Invalid or inappropriate API flags specified.
- [var errSecCSInvalidObjectRef: OSStatus](errseccsinvalidobjectref.md)
  Invalid API object reference.
- [var errSecCSInvalidPlatform: OSStatus](errseccsinvalidplatform.md)
  Invalid platform identifier or platform mismatch.
- [var errSecCSMultipleGuests: OSStatus](errseccsmultipleguests.md)
  Code signing host has more than one block of guest code with this attribute value.
- [var errSecCSNoMatches: OSStatus](errseccsnomatches.md)
  No matches were found for a search or update operation.
- [var errSecCSNoSuchCode: OSStatus](errseccsnosuchcode.md)
  Code signing host has no guest code with the requested attributes.
- [var errSecCSNotAHost: OSStatus](errseccsnotahost.md)
  This code is not a code signing host.
- [var errSecCSNotAppLike: OSStatus](errseccsnotapplike.md)
  The code is valid but does not seem to be an app.
- [var errSecCSNotSupported: OSStatus](errseccsnotsupported.md)
  Operation not supported for this type of code.
- [var errSecCSObjectRequired: OSStatus](errseccsobjectrequired.md)
  A required pointer argument was null.
- [var errSecCSOutdated: OSStatus](errseccsoutdated.md)
  The presented data is out of date.
- [var errSecCSReqFailed: OSStatus](errseccsreqfailed.md)
  The code failed to satisfy one of the code requirements.
- [var errSecCSReqInvalid: OSStatus](errseccsreqinvalid.md)
  Invalid or corrupted code requirements.
- [var errSecCSReqUnsupported: OSStatus](errseccsrequnsupported.md)
  Unsupported type or version of code requirements.
- [var errSecCSStaticCodeChanged: OSStatus](errseccsstaticcodechanged.md)
  The code on disk has been modified after the code started running.
- [var errSecCSStaticCodeNotFound: OSStatus](errseccsstaticcodenotfound.md)
  Cannot find code object on disk.
- [var errSecCSTooBig: OSStatus](errseccstoobig.md)
  The code is too big for current signing format.
- [var errSecCSUnimplemented: OSStatus](errseccsunimplemented.md)
  Unimplemented code signing feature.
- [var errSecCSUnsupportedGuestAttributes: OSStatus](errseccsunsupportedguestattributes.md)
  Cannot locate guest code using this attribute set.
- [var errSecCSVetoed: OSStatus](errseccsvetoed.md)
- [var errSecCSWeakResourceEnvelope: OSStatus](errseccsweakresourceenvelope.md)
  The resource envelope is obsolete (version 1 signature).
- [var errSecCSWeakResourceRules: OSStatus](errseccsweakresourcerules.md)
  The resource envelope is obsolete (custom omit rules).
- [var errSecCSBadTeamIdentifier: OSStatus](errseccsbadteamidentifier.md)
  A Team Identifier is wrong or inappropriate.
- [var errSecCSInvalidAssociatedFileData: OSStatus](errseccsinvalidassociatedfiledata.md)
  Resource fork, Finder information, or similar detritus not allowed.
- [var errSecCSInvalidTeamIdentifier: OSStatus](errseccsinvalidteamidentifier.md)
  A Team Identifier string is invalid.
- [var errSecMultipleExecSegments: OSStatus](errsecmultipleexecsegments.md)
  The image contains multiple executable segments.
- [var errSecCSInvalidEntitlements: OSStatus](errseccsinvalidentitlements.md)
  Encountered an invalid entitlement plist.
- [var errSecCSInvalidRuntimeVersion: OSStatus](errseccsinvalidruntimeversion.md)
  An invalid runtime version was explicity set.
- [var errSecCSRevokedNotarization: OSStatus](errseccsrevokednotarization.md)
  Notarization indicates this code has been revoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/code-signing-services-result-codes)*