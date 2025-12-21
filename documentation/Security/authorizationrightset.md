# AuthorizationRightSet(_:_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Creates or updates a right entry in the policy database.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func AuthorizationRightSet(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<CChar>, _ rightDefinition: CFTypeRef, _ descriptionKey: CFString?, _ bundle: CFBundle?, _ localeTableName: CFString?) -> OSStatus
```

## Mentions

- [Extending authorization services with plug-ins](extending-authorization-services-with-plug-ins.md)

#### Return Value

A result code. See [`Authorization Services Result Codes`](authorization-services-result-codes.md).

#### Discussion

The right you create must be an explicit right with no wildcards. Wildcard rights are for use by system administrators for site configuration. You can use this function to create a new right or modify an existing right. For example:

```c
AuthorizationRightSet(NULL, "com.ifoo.ifax.send",
CFSTR(kAuthorizationRuleIsAdmin), CFSTR("Authorize sending  of a fax"), NULL, NULL);
```

adds a rule for letting administrators send faxes. This example creates a right named `“com.ifoo.ifax.send”` and sets the rules to require the user to be an administrator by using the [`kAuthorizationRuleIsAdmin`](kauthorizationruleisadmin.md) constant. This example also sets a comment to let the system administrator know that the right authorizes administrators to send a fax.

Because the first parameter is `NULL`, a new [`AuthorizationRef`](authorizationref.md) object is created internally and disposed of. If you need to further use the object (for example, when calling [`AuthorizationExecuteWithPrivileges`](authorizationexecutewithprivileges.md)), you must explicitly create the object and pass it in as the first argument to [`AuthorizationRightSet(_:_:_:_:_:_:)`](authorizationrightset(_:_:_:_:_:_:).md), then free it with a call to [`AuthorizationFree(_:_:)`](authorizationfree(_:_:).md).

To specify additional attributes for the right, you can pass a dictionary in the `rightDefinition` parameter as shown in the following example.

```c
CFStringRef keys[2] = {CFSTR(kRightRule), CFSTR(kRightComment)};
CFStringRef values[2] = {CFSTR(kAuthorizationRuleIsAdmin), CFSTR("authorizes  sending of 1 fax message")};
AuthorizationRef authRef;
CFDictionaryRef aDict;
aDict = CFDictionaryCreate(NULL, (void *)keys, (void *)values, 2,  &kCFCopyStringDictionaryKeyCallBacks, &kCFTypeDictionaryValueCallBacks);
AuthorizationCreate(NULL, NULL, 0, &authRef);
AuthorizationRightSet(authRef, "com.ifoo.ifax.send", aDict,  CFSTR("Authorize sending  of a fax"), NULL, NULL);
CFRelease(aDict);
...
AuthorizationFree(authRef, kAuthorizationFlagDefaults);
```

This call creates the same right as before, but adds a specific right comment to the rules definition.

When you specify comments, you should be specific about what you need to authorize. For example, the means of proof required for [`kAuthorizationRuleAuthenticateAsAdmin`](kauthorizationruleauthenticateasadmin.md) (a username and password) should not be included here since that rule might be configured differently.

## Parameters

- `authRef`: A valid authorization reference used to authorize modifications.
- `rightName`: An ASCII character string representing the right name. The policy database does not accept wildcard right names.
- `rightDefinition`: Either a   containing keys defining the rules or a   representing the name of another right whose rules you wish to duplicate. See   for some possible values.
- `descriptionKey`: A string used as a key for looking up localized descriptions. If no localization is found, this is the description itself. This parameter is optional; pass   if you do not require it.
- `bundle`: A bundle to get localizations from if not the main bundle. This parameter is optional; pass   if you do not require it.
- `localeTableName`: A string representing a table name from which to get localizations. This parameter is optional; pass   if you have no localizations or you wish to use the localizations available in  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/authorizationrightset(_:_:_:_:_:_:))*