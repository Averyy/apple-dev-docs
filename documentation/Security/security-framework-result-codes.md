# Security Framework Result Codes

**Framework**: Security

Evaluate result codes common to many Security framework functions.

#### Discussion

Use the [`SecCopyErrorMessageString(_:_:)`](seccopyerrormessagestring(_:_:).md) function to obtain a human readable string corresponding to these status codes.

In addition to the codes listed here, certain Security framework services provide additional status codes that are specific to that service. In particular, see [`Authorization Services Result Codes`](authorization-services-result-codes.md), [`Sessions API Result Codes`](sessions-api-result-codes.md), [`Secure Transport Result Codes`](secure-transport-result-codes.md), [`Secure Download Result Codes`](secure-download-result-codes.md), and [`Code Signing Services Result Codes`](code-signing-services-result-codes.md).

## Topics

### Result Strings
- [func SecCopyErrorMessageString(OSStatus, UnsafeMutableRawPointer?) -> CFString?](seccopyerrormessagestring(_:_:).md)
  Returns a string explaining the meaning of a security result code.
### System Result Codes
- [var errSecSuccess: OSStatus](errsecsuccess.md)
  No error.
- [var errSecUnimplemented: OSStatus](errsecunimplemented.md)
  A function or operation is not implemented.
- [var errSecDskFull: OSStatus](errsecdskfull.md)
  The disk is full.
- [var errSecDiskFull: OSStatus](errsecdiskfull.md)
  The disk is full.
- [var errSecIO: OSStatus](errsecio.md)
  I/O error.
- [var errSecOpWr: OSStatus](errsecopwr.md)
  The file is already open with write permission.
- [var errSecParam: OSStatus](errsecparam.md)
  One or more parameters passed to the function are not valid.
- [var errSecWrPerm: OSStatus](errsecwrperm.md)
  Write permissions error.
- [var errSecAllocate: OSStatus](errsecallocate.md)
  Failed to allocate memory.
- [var errSecUserCanceled: OSStatus](errsecusercanceled.md)
  User canceled the operation.
- [var errSecBadReq: OSStatus](errsecbadreq.md)
  Bad parameter or invalid state for operation.
### Internal Error Result Codes
- [var errSecInternalComponent: OSStatus](errsecinternalcomponent.md)
  An internal component experienced an error.
- [var errSecCoreFoundationUnknown: OSStatus](errseccorefoundationunknown.md)
  An unknown Core Foundation error occurred.
- [var errSecInternalError: OSStatus](errsecinternalerror.md)
  An internal error occurred.
### Keychain Result Codes
- [var errSecNotAvailable: OSStatus](errsecnotavailable.md)
  No trust results are available.
- [var errSecReadOnly: OSStatus](errsecreadonly.md)
  Read-only error.
- [var errSecAuthFailed: OSStatus](errsecauthfailed.md)
  Authorization and/or authentication failed.
- [var errSecNoSuchKeychain: OSStatus](errsecnosuchkeychain.md)
  The keychain does not exist.
- [var errSecInvalidKeychain: OSStatus](errsecinvalidkeychain.md)
  The keychain is not valid.
- [var errSecDuplicateKeychain: OSStatus](errsecduplicatekeychain.md)
  A keychain with the same name already exists.
- [var errSecDuplicateCallback: OSStatus](errsecduplicatecallback.md)
  More than one callback of the same name exists.
- [var errSecInvalidCallback: OSStatus](errsecinvalidcallback.md)
  The callback is not valid.
- [var errSecDuplicateItem: OSStatus](errsecduplicateitem.md)
  The item already exists.
- [var errSecItemNotFound: OSStatus](errsecitemnotfound.md)
  The item cannot be found.
- [var errSecBufferTooSmall: OSStatus](errsecbuffertoosmall.md)
  The buffer is too small.
- [var errSecDataTooLarge: OSStatus](errsecdatatoolarge.md)
  The data is too large for the particular data type.
- [var errSecNoSuchAttr: OSStatus](errsecnosuchattr.md)
  The attribute does not exist.
- [var errSecInvalidItemRef: OSStatus](errsecinvaliditemref.md)
  The item reference is invalid.
- [var errSecInvalidSearchRef: OSStatus](errsecinvalidsearchref.md)
  The search reference is invalid.
- [var errSecNoSuchClass: OSStatus](errsecnosuchclass.md)
  The keychain item class does not exist.
- [var errSecNoDefaultKeychain: OSStatus](errsecnodefaultkeychain.md)
  A default keychain does not exist.
- [var errSecInteractionNotAllowed: OSStatus](errsecinteractionnotallowed.md)
  Interaction with the Security Server is not allowed.
- [var errSecReadOnlyAttr: OSStatus](errsecreadonlyattr.md)
  The attribute is read-only.
- [var errSecWrongSecVersion: OSStatus](errsecwrongsecversion.md)
  The version is incorrect.
- [var errSecKeySizeNotAllowed: OSStatus](errseckeysizenotallowed.md)
  The key size is not allowed.
- [var errSecNoStorageModule: OSStatus](errsecnostoragemodule.md)
  There is no storage module available.
- [var errSecNoCertificateModule: OSStatus](errsecnocertificatemodule.md)
  There is no certificate module available.
- [var errSecNoPolicyModule: OSStatus](errsecnopolicymodule.md)
  There is no policy module available.
- [var errSecInteractionRequired: OSStatus](errsecinteractionrequired.md)
  User interaction is required.
- [var errSecDataNotAvailable: OSStatus](errsecdatanotavailable.md)
  The data is not available.
- [var errSecDataNotModifiable: OSStatus](errsecdatanotmodifiable.md)
  The data is not modifiable.
- [var errSecCreateChainFailed: OSStatus](errseccreatechainfailed.md)
  The attempt to create a certificate chain failed.
- [var errSecInvalidPrefsDomain: OSStatus](errsecinvalidprefsdomain.md)
  The preference domain specified is invalid.
- [var errSecInDarkWake: OSStatus](errsecindarkwake.md)
  The user interface cannot be displayed because the system is in a dark wake state.
### Certificate Result Codes
- [var errSecUnknownCriticalExtensionFlag: OSStatus](errsecunknowncriticalextensionflag.md)
  There is an unknown critical extension flag.
- [var errSecCertificateCannotOperate: OSStatus](errseccertificatecannotoperate.md)
  The certificate cannot operate.
- [var errSecCertificateExpired: OSStatus](errseccertificateexpired.md)
  An expired certificate was detected.
- [var errSecCertificateNotValidYet: OSStatus](errseccertificatenotvalidyet.md)
  The certificate is not yet valid.
- [var errSecCertificateRevoked: OSStatus](errseccertificaterevoked.md)
  The certificate was revoked.
- [var errSecCertificateSuspended: OSStatus](errseccertificatesuspended.md)
  The certificate was suspended.
- [var errSecInvalidCertAuthority: OSStatus](errsecinvalidcertauthority.md)
  The certificate authority is not valid.
- [var errSecInvalidCertificateGroup: OSStatus](errsecinvalidcertificategroup.md)
  An invalid certificate group was detected.
- [var errSecInvalidCertificateRef: OSStatus](errsecinvalidcertificateref.md)
  An invalid certificate reference was detected.
- [var errSecCertificateNameNotAllowed: OSStatus](errseccertificatenamenotallowed.md)
  The requested name isn’t allowed for this certificate.
- [var errSecCertificatePolicyNotAllowed: OSStatus](errseccertificatepolicynotallowed.md)
  The requested policy isn’t allowed for this certificate.
- [var errSecCertificateValidityPeriodTooLong: OSStatus](errseccertificatevalidityperiodtoolong.md)
  The validity period in the certificate exceeds the maximum allowed period.
### ACL Result Codes
- [var errSecACLAddFailed: OSStatus](errsecacladdfailed.md)
  An ACL add operation failed.
- [var errSecACLChangeFailed: OSStatus](errsecaclchangefailed.md)
  An ACL change operation failed.
- [var errSecACLDeleteFailed: OSStatus](errsecacldeletefailed.md)
  An ACL delete operation failed.
- [var errSecACLNotSimple: OSStatus](errsecaclnotsimple.md)
  The access control list is not in standard simple form.
- [var errSecACLReplaceFailed: OSStatus](errsecaclreplacefailed.md)
  An ACL replace operation failed.
- [var errSecAppleAddAppACLSubject: OSStatus](errsecappleaddappaclsubject.md)
  Adding an application ACL subject failed.
- [var errSecInvalidBaseACLs: OSStatus](errsecinvalidbaseacls.md)
  The base access control lists are not valid.
- [var errSecInvalidACL: OSStatus](errsecinvalidacl.md)
  An invalid access control list was detected.
### CRL Result Codes
- [var errSecCRLExpired: OSStatus](errseccrlexpired.md)
  The certificate revocation list has expired.
- [var errSecCRLNotValidYet: OSStatus](errseccrlnotvalidyet.md)
  The certificate revocation list is not yet valid.
- [var errSecCRLNotFound: OSStatus](errseccrlnotfound.md)
  The certificate revocation list was not found.
- [var errSecCRLServerDown: OSStatus](errseccrlserverdown.md)
  The certificate revocation list server is down.
- [var errSecCRLBadURI: OSStatus](errseccrlbaduri.md)
  The certificate revocation list has a bad uniform resource identifier.
- [var errSecCRLNotTrusted: OSStatus](errseccrlnottrusted.md)
  The certificate revocation list is not trusted.
- [var errSecUnknownCertExtension: OSStatus](errsecunknowncertextension.md)
  An unknown certificate extension was detected.
- [var errSecUnknownCRLExtension: OSStatus](errsecunknowncrlextension.md)
  An unknown certificate revocation list extension was detected.
- [var errSecCRLPolicyFailed: OSStatus](errseccrlpolicyfailed.md)
  The certificate revocation list policy failed.
- [var errSecCRLAlreadySigned: OSStatus](errseccrlalreadysigned.md)
  The certificate revocation list is already signed.
- [var errSecIDPFailure: OSStatus](errsecidpfailure.md)
  The issuing distribution point is not valid.
- [var errSecInvalidCRLEncoding: OSStatus](errsecinvalidcrlencoding.md)
  The certificate revocation list encoding is not valid.
- [var errSecInvalidCRLType: OSStatus](errsecinvalidcrltype.md)
  The certificate revocation list type is not valid.
- [var errSecInvalidCRL: OSStatus](errsecinvalidcrl.md)
  The certificate revocation list is not valid.
- [var errSecInvalidCRLGroup: OSStatus](errsecinvalidcrlgroup.md)
  An invalid certificate revocation list group was detected.
- [var errSecInvalidCRLIndex: OSStatus](errsecinvalidcrlindex.md)
  The certificate revocation list index is not valid.
- [var errSecInvaldCRLAuthority: OSStatus](errsecinvaldcrlauthority.md)
  The certificate revocation list authority is not valid.
### SMIME Result Codes
- [var errSecSMIMEEmailAddressesNotFound: OSStatus](errsecsmimeemailaddressesnotfound.md)
  An email address mismatch was detected.
- [var errSecSMIMEBadExtendedKeyUsage: OSStatus](errsecsmimebadextendedkeyusage.md)
  The appropriate extended key usage for SMIME is not found.
- [var errSecSMIMEBadKeyUsage: OSStatus](errsecsmimebadkeyusage.md)
  The key usage is not compatible with SMIME.
- [var errSecSMIMEKeyUsageNotCritical: OSStatus](errsecsmimekeyusagenotcritical.md)
  The key usage extension is not marked as critical.
- [var errSecSMIMENoEmailAddress: OSStatus](errsecsmimenoemailaddress.md)
  No email address is found in the certificate.
- [var errSecSMIMESubjAltNameNotCritical: OSStatus](errsecsmimesubjaltnamenotcritical.md)
  The subject alternative name extension is not marked as critical.
- [var errSecSSLBadExtendedKeyUsage: OSStatus](errsecsslbadextendedkeyusage.md)
  The appropriate extended key usage for SSL is not found.
### OCSP Result Codes
- [var errSecOCSPBadResponse: OSStatus](errsecocspbadresponse.md)
  The online certificate status protocol (OCSP) response is incorrect or cannot be parsed.
- [var errSecOCSPBadRequest: OSStatus](errsecocspbadrequest.md)
  The online certificate status protocol (OCSP) request is incorrect or cannot be parsed.
- [var errSecOCSPUnavailable: OSStatus](errsecocspunavailable.md)
  The online certificate status protocol (OCSP) service is unavailable.
- [var errSecOCSPStatusUnrecognized: OSStatus](errsecocspstatusunrecognized.md)
  The online certificate status protocol (OCSP) server does not recognize this certificate.
- [var errSecEndOfData: OSStatus](errsecendofdata.md)
  An end-of-data was detected.
- [var errSecIncompleteCertRevocationCheck: OSStatus](errsecincompletecertrevocationcheck.md)
  An incomplete certificate revocation check occurred.
- [var errSecNetworkFailure: OSStatus](errsecnetworkfailure.md)
  A network failure occurred.
- [var errSecOCSPNotTrustedToAnchor: OSStatus](errsecocspnottrustedtoanchor.md)
  The online certificate status protocol (OCSP) response is not trusted to a root or anchor certificate.
- [var errSecRecordModified: OSStatus](errsecrecordmodified.md)
  The record is modified.
- [var errSecOCSPSignatureError: OSStatus](errsecocspsignatureerror.md)
  The online certificate status protocol (OCSP) response has an invalid signature.
- [var errSecOCSPNoSigner: OSStatus](errsecocspnosigner.md)
  The online certificate status protocol (OCSP) response has no signer.
- [var errSecOCSPResponderMalformedReq: OSStatus](errsecocsprespondermalformedreq.md)
  The online certificate status protocol (OCSP) responder detected a malformed request.
- [var errSecOCSPResponderInternalError: OSStatus](errsecocspresponderinternalerror.md)
  The online certificate status protocol (OCSP) responder detected an internal error.
- [var errSecOCSPResponderTryLater: OSStatus](errsecocsprespondertrylater.md)
  The online certificate status protocol (OCSP) responder is busy, try again later.
- [var errSecOCSPResponderSignatureRequired: OSStatus](errsecocsprespondersignaturerequired.md)
  The online certificate status protocol (OCSP) responder requires a signature.
- [var errSecOCSPResponderUnauthorized: OSStatus](errsecocspresponderunauthorized.md)
  The online certificate status protocol (OCSP) responder rejects the request as unauthorized.
- [var errSecOCSPResponseNonceMismatch: OSStatus](errsecocspresponsenoncemismatch.md)
  The online certificate status protocol (OCSP) response nonce does not match the request.
### Code Signing Result Codes
- [var errSecCodeSigningBadCertChainLength: OSStatus](errseccodesigningbadcertchainlength.md)
  Code signing encountered an incorrect certificate chain length.
- [var errSecCodeSigningNoBasicConstraints: OSStatus](errseccodesigningnobasicconstraints.md)
  Code signing found no basic constraints.
- [var errSecCodeSigningBadPathLengthConstraint: OSStatus](errseccodesigningbadpathlengthconstraint.md)
  Code signing encountered an incorrect path length constraint.
- [var errSecCodeSigningNoExtendedKeyUsage: OSStatus](errseccodesigningnoextendedkeyusage.md)
  Code signing found no extended key usage.
- [var errSecCodeSigningDevelopment: OSStatus](errseccodesigningdevelopment.md)
  Code signing indicated use of a development-only certificate.
- [var errSecResourceSignBadCertChainLength: OSStatus](errsecresourcesignbadcertchainlength.md)
  Resource signing detects an incorrect certificate chain length.
- [var errSecResourceSignBadExtKeyUsage: OSStatus](errsecresourcesignbadextkeyusage.md)
  Resource signing detects an error in the extended key usage.
- [var errSecTrustSettingDeny: OSStatus](errsectrustsettingdeny.md)
  The trust setting for this policy is set to Deny.
- [var errSecInvalidSubjectName: OSStatus](errsecinvalidsubjectname.md)
  An invalid certificate subject name was detected.
- [var errSecUnknownQualifiedCertStatement: OSStatus](errsecunknownqualifiedcertstatement.md)
  An unknown qualified certificate statement was detected.
### Mobile Me Result Codes
- [var errSecMobileMeRequestQueued: OSStatus](errsecmobilemerequestqueued.md)
  The MobileMe request will be sent during the next connection.
- [var errSecMobileMeRequestRedirected: OSStatus](errsecmobilemerequestredirected.md)
  The MobileMe request was redirected.
- [var errSecMobileMeServerError: OSStatus](errsecmobilemeservererror.md)
  A MobileMe server error occurred.
- [var errSecMobileMeServerNotAvailable: OSStatus](errsecmobilemeservernotavailable.md)
  The MobileMe server is not available.
- [var errSecMobileMeServerAlreadyExists: OSStatus](errsecmobilemeserveralreadyexists.md)
  The MobileMe server reported that the item already exists.
- [var errSecMobileMeServerServiceErr: OSStatus](errsecmobilemeserverserviceerr.md)
  A MobileMe service error occurred.
- [var errSecMobileMeRequestAlreadyPending: OSStatus](errsecmobilemerequestalreadypending.md)
  A MobileMe request is already pending.
- [var errSecMobileMeNoRequestPending: OSStatus](errsecmobilemenorequestpending.md)
  MobileMe has no request pending.
- [var errSecMobileMeCSRVerifyFailure: OSStatus](errsecmobilemecsrverifyfailure.md)
  A MobileMe certificate signing request verification failure occurred.
- [var errSecMobileMeFailedConsistencyCheck: OSStatus](errsecmobilemefailedconsistencycheck.md)
  MobileMe found a failed consistency check.
### Cryptographic Key Result Codes
- [var errSecKeyUsageIncorrect: OSStatus](errseckeyusageincorrect.md)
  The key usage is incorrect.
- [var errSecKeyBlobTypeIncorrect: OSStatus](errseckeyblobtypeincorrect.md)
  The key blob type is incorrect.
- [var errSecKeyHeaderInconsistent: OSStatus](errseckeyheaderinconsistent.md)
  The key header is inconsistent.
- [var errSecKeyIsSensitive: OSStatus](errseckeyissensitive.md)
  The key must be wrapped to be exported.
- [var errSecUnsupportedKeyFormat: OSStatus](errsecunsupportedkeyformat.md)
  The key header format is not supported.
- [var errSecUnsupportedKeySize: OSStatus](errsecunsupportedkeysize.md)
  The key size is not supported.
- [var errSecInvalidKeyUsageMask: OSStatus](errsecinvalidkeyusagemask.md)
  The key usage mask is not valid.
- [var errSecUnsupportedKeyUsageMask: OSStatus](errsecunsupportedkeyusagemask.md)
  The key usage mask is not supported.
- [var errSecInvalidKeyAttributeMask: OSStatus](errsecinvalidkeyattributemask.md)
  The key attribute mask is not valid.
- [var errSecUnsupportedKeyAttributeMask: OSStatus](errsecunsupportedkeyattributemask.md)
  The key attribute mask is not supported.
- [var errSecInvalidKeyLabel: OSStatus](errsecinvalidkeylabel.md)
  The key label is not valid.
- [var errSecUnsupportedKeyLabel: OSStatus](errsecunsupportedkeylabel.md)
  The key label is not supported.
- [var errSecInvalidKeyFormat: OSStatus](errsecinvalidkeyformat.md)
  The key format is not valid.
- [var errSecInvalidKeyBlob: OSStatus](errsecinvalidkeyblob.md)
  The specified database has an invalid key blob.
- [var errSecInvalidKeyHierarchy: OSStatus](errsecinvalidkeyhierarchy.md)
  An invalid key hierarchy was detected.
- [var errSecInvalidKeyRef: OSStatus](errsecinvalidkeyref.md)
  An invalid key was encountered.
- [var errSecInvalidKeyUsageForPolicy: OSStatus](errsecinvalidkeyusageforpolicy.md)
  The key usage is not valid for the specified policy.
### Invalid Attribute Result Codes
- [var errSecInvalidAttributeKey: OSStatus](errsecinvalidattributekey.md)
  A key attribute is not valid.
- [var errSecInvalidAttributeInitVector: OSStatus](errsecinvalidattributeinitvector.md)
  An init vector attribute is not valid.
- [var errSecInvalidAttributeSalt: OSStatus](errsecinvalidattributesalt.md)
  A salt attribute is not valid.
- [var errSecInvalidAttributePadding: OSStatus](errsecinvalidattributepadding.md)
  A padding attribute is not valid.
- [var errSecInvalidAttributeRandom: OSStatus](errsecinvalidattributerandom.md)
  A random number attribute is not valid.
- [var errSecInvalidAttributeSeed: OSStatus](errsecinvalidattributeseed.md)
  A seed attribute is not valid.
- [var errSecInvalidAttributePassphrase: OSStatus](errsecinvalidattributepassphrase.md)
  A passphrase attribute is not valid.
- [var errSecInvalidAttributeKeyLength: OSStatus](errsecinvalidattributekeylength.md)
  A key length attribute is not valid.
- [var errSecInvalidAttributeBlockSize: OSStatus](errsecinvalidattributeblocksize.md)
  A block size attribute is not valid.
- [var errSecInvalidAttributeOutputSize: OSStatus](errsecinvalidattributeoutputsize.md)
  An output size attribute is not valid.
- [var errSecInvalidAttributeRounds: OSStatus](errsecinvalidattributerounds.md)
  The number of rounds attribute is not valid.
- [var errSecInvalidAlgorithmParms: OSStatus](errsecinvalidalgorithmparms.md)
  An algorithm parameters attribute is not valid.
- [var errSecInvalidAttributeLabel: OSStatus](errsecinvalidattributelabel.md)
  A label attribute is not valid.
- [var errSecInvalidAttributeKeyType: OSStatus](errsecinvalidattributekeytype.md)
  A key type attribute is not valid.
- [var errSecInvalidAttributeMode: OSStatus](errsecinvalidattributemode.md)
  A mode attribute is not valid.
- [var errSecInvalidAttributeEffectiveBits: OSStatus](errsecinvalidattributeeffectivebits.md)
  An effective bits attribute is not valid.
- [var errSecInvalidAttributeStartDate: OSStatus](errsecinvalidattributestartdate.md)
  A start date attribute is not valid.
- [var errSecInvalidAttributeEndDate: OSStatus](errsecinvalidattributeenddate.md)
  An end date attribute is not valid.
- [var errSecInvalidAttributeVersion: OSStatus](errsecinvalidattributeversion.md)
  A version attribute is not valid.
- [var errSecInvalidAttributePrime: OSStatus](errsecinvalidattributeprime.md)
  A prime attribute is not valid.
- [var errSecInvalidAttributeBase: OSStatus](errsecinvalidattributebase.md)
  A base attribute is not valid.
- [var errSecInvalidAttributeSubprime: OSStatus](errsecinvalidattributesubprime.md)
  A subprime attribute is not valid.
- [var errSecInvalidAttributeIterationCount: OSStatus](errsecinvalidattributeiterationcount.md)
  An iteration count attribute is not valid.
- [var errSecInvalidAttributeDLDBHandle: OSStatus](errsecinvalidattributedldbhandle.md)
  A database handle attribute is not valid.
- [var errSecInvalidAttributeAccessCredentials: OSStatus](errsecinvalidattributeaccesscredentials.md)
  An access credentials attribute is not valid.
- [var errSecInvalidAttributePublicKeyFormat: OSStatus](errsecinvalidattributepublickeyformat.md)
  A public key format attribute is not valid.
- [var errSecInvalidAttributePrivateKeyFormat: OSStatus](errsecinvalidattributeprivatekeyformat.md)
  A private key format attribute is not valid.
- [var errSecInvalidAttributeSymmetricKeyFormat: OSStatus](errsecinvalidattributesymmetrickeyformat.md)
  A symmetric key format attribute is not valid.
- [var errSecInvalidAttributeWrappedKeyFormat: OSStatus](errsecinvalidattributewrappedkeyformat.md)
  A wrapped key format attribute is not valid.
### Missing Attribute Result Codes
- [var errSecMissingAttributeKey: OSStatus](errsecmissingattributekey.md)
  A key attribute is missing.
- [var errSecMissingAttributeInitVector: OSStatus](errsecmissingattributeinitvector.md)
  An init vector attribute is missing.
- [var errSecMissingAttributeSalt: OSStatus](errsecmissingattributesalt.md)
  A salt attribute is missing.
- [var errSecMissingAttributePadding: OSStatus](errsecmissingattributepadding.md)
  A padding attribute is missing.
- [var errSecMissingAttributeRandom: OSStatus](errsecmissingattributerandom.md)
  A random number attribute is missing.
- [var errSecMissingAttributeSeed: OSStatus](errsecmissingattributeseed.md)
  A seed attribute is missing.
- [var errSecMissingAttributePassphrase: OSStatus](errsecmissingattributepassphrase.md)
  A passphrase attribute is missing.
- [var errSecMissingAttributeKeyLength: OSStatus](errsecmissingattributekeylength.md)
  A key length attribute is missing.
- [var errSecMissingAttributeBlockSize: OSStatus](errsecmissingattributeblocksize.md)
  A block size attribute is missing.
- [var errSecMissingAttributeOutputSize: OSStatus](errsecmissingattributeoutputsize.md)
  An output size attribute is missing.
- [var errSecMissingAttributeRounds: OSStatus](errsecmissingattributerounds.md)
  The number of rounds attribute is missing.
- [var errSecMissingAlgorithmParms: OSStatus](errsecmissingalgorithmparms.md)
  An algorithm parameters attribute is missing.
- [var errSecMissingAttributeLabel: OSStatus](errsecmissingattributelabel.md)
  A label attribute is missing.
- [var errSecMissingAttributeKeyType: OSStatus](errsecmissingattributekeytype.md)
  A key type attribute is missing.
- [var errSecMissingAttributeMode: OSStatus](errsecmissingattributemode.md)
  A mode attribute is missing.
- [var errSecMissingAttributeEffectiveBits: OSStatus](errsecmissingattributeeffectivebits.md)
  An effective bits attribute is missing.
- [var errSecMissingAttributeStartDate: OSStatus](errsecmissingattributestartdate.md)
  A start date attribute is missing.
- [var errSecMissingAttributeEndDate: OSStatus](errsecmissingattributeenddate.md)
  An end date attribute is missing.
- [var errSecMissingAttributeVersion: OSStatus](errsecmissingattributeversion.md)
  A version attribute is missing.
- [var errSecMissingAttributePrime: OSStatus](errsecmissingattributeprime.md)
  A prime attribute is missing.
- [var errSecMissingAttributeBase: OSStatus](errsecmissingattributebase.md)
  A base attribute is missing.
- [var errSecMissingAttributeSubprime: OSStatus](errsecmissingattributesubprime.md)
  A subprime attribute is missing.
- [var errSecMissingAttributeIterationCount: OSStatus](errsecmissingattributeiterationcount.md)
  An iteration count attribute is missing.
- [var errSecMissingAttributeDLDBHandle: OSStatus](errsecmissingattributedldbhandle.md)
  A database handle attribute is missing.
- [var errSecMissingAttributeAccessCredentials: OSStatus](errsecmissingattributeaccesscredentials.md)
  An access credentials attribute is missing.
- [var errSecMissingAttributePublicKeyFormat: OSStatus](errsecmissingattributepublickeyformat.md)
  A public key format attribute is missing.
- [var errSecMissingAttributePrivateKeyFormat: OSStatus](errsecmissingattributeprivatekeyformat.md)
  A private key format attribute is missing.
- [var errSecMissingAttributeSymmetricKeyFormat: OSStatus](errsecmissingattributesymmetrickeyformat.md)
  A symmetric key format attribute is missing.
- [var errSecMissingAttributeWrappedKeyFormat: OSStatus](errsecmissingattributewrappedkeyformat.md)
  A wrapped key format attribute is missing.
### Timestamp Result Codes
- [var errSecTimestampMissing: OSStatus](errsectimestampmissing.md)
  A timestamp is expected but is not found.
- [var errSecTimestampInvalid: OSStatus](errsectimestampinvalid.md)
  The timestamp is not valid.
- [var errSecTimestampNotTrusted: OSStatus](errsectimestampnottrusted.md)
  The timestamp is not trusted.
- [var errSecTimestampServiceNotAvailable: OSStatus](errsectimestampservicenotavailable.md)
- [var errSecTimestampBadAlg: OSStatus](errsectimestampbadalg.md)
  Found an unrecognized or unsupported algorithm identifier (AI) in timestamp.
- [var errSecTimestampBadRequest: OSStatus](errsectimestampbadrequest.md)
  The timestamp transaction is not permitted or supported.
- [var errSecTimestampBadDataFormat: OSStatus](errsectimestampbaddataformat.md)
  The timestamp data submitted has the wrong format.
- [var errSecTimestampTimeNotAvailable: OSStatus](errsectimestamptimenotavailable.md)
  The time source for the timestamp authority is not available.
- [var errSecTimestampUnacceptedPolicy: OSStatus](errsectimestampunacceptedpolicy.md)
  The requested policy is not supported by the timestamp authority.
- [var errSecTimestampUnacceptedExtension: OSStatus](errsectimestampunacceptedextension.md)
  The requested extension is not supported by the timestamp authority.
- [var errSecTimestampAddInfoNotAvailable: OSStatus](errsectimestampaddinfonotavailable.md)
  The additional information requested is not available.
- [var errSecTimestampSystemFailure: OSStatus](errsectimestampsystemfailure.md)
  The timestamp request cannot be handled due to a system failure.
- [var errSecSigningTimeMissing: OSStatus](errsecsigningtimemissing.md)
  A signing time is missing.
- [var errSecTimestampRejection: OSStatus](errsectimestamprejection.md)
  A timestamp transaction is rejected.
- [var errSecTimestampWaiting: OSStatus](errsectimestampwaiting.md)
  A timestamp transaction is waiting.
- [var errSecTimestampRevocationWarning: OSStatus](errsectimestamprevocationwarning.md)
  A timestamp authority revocation warning is issued.
- [var errSecTimestampRevocationNotification: OSStatus](errsectimestamprevocationnotification.md)
  A timestamp authority revocation notification is issued.
### Invalid parameter result codes
- [var errSecInvalidAction: OSStatus](errsecinvalidaction.md)
  The action is invalid.
- [var errSecInvalidAddinFunctionTable: OSStatus](errsecinvalidaddinfunctiontable.md)
  An invalid add-in function table was detected.
- [var errSecInvalidAlgorithm: OSStatus](errsecinvalidalgorithm.md)
  An invalid algorithm was detected.
- [var errSecInvalidAuthority: OSStatus](errsecinvalidauthority.md)
  The authority is not valid.
- [var errSecInvalidAuthorityKeyID: OSStatus](errsecinvalidauthoritykeyid.md)
  The authority key ID is not valid.
- [var errSecInvalidBundleInfo: OSStatus](errsecinvalidbundleinfo.md)
  The bundle information is not valid.
- [var errSecInvalidContext: OSStatus](errsecinvalidcontext.md)
  An invalid context was detected.
- [var errSecInvalidDBList: OSStatus](errsecinvaliddblist.md)
  An invalid DB list was detected.
- [var errSecInvalidDBLocation: OSStatus](errsecinvaliddblocation.md)
  The database location is not valid.
- [var errSecInvalidData: OSStatus](errsecinvaliddata.md)
  Invalid data was detected.
- [var errSecInvalidDatabaseBlob: OSStatus](errsecinvaliddatabaseblob.md)
  The specified database has an invalid blob.
- [var errSecInvalidDigestAlgorithm: OSStatus](errsecinvaliddigestalgorithm.md)
  An invalid digest algorithm was detected.
- [var errSecInvalidEncoding: OSStatus](errsecinvalidencoding.md)
  The encoding is not valid.
- [var errSecInvalidExtendedKeyUsage: OSStatus](errsecinvalidextendedkeyusage.md)
  The extended key usage is not valid.
- [var errSecInvalidFormType: OSStatus](errsecinvalidformtype.md)
  The form type is not valid.
- [var errSecInvalidGUID: OSStatus](errsecinvalidguid.md)
  An invalid GUID was detected.
- [var errSecInvalidHandle: OSStatus](errsecinvalidhandle.md)
  An invalid handle was encountered.
- [var errSecInvalidHandleUsage: OSStatus](errsecinvalidhandleusage.md)
  The common security services manager handle does not match with the service type.
- [var errSecInvalidID: OSStatus](errsecinvalidid.md)
  The ID is not valid.
- [var errSecInvalidIDLinkage: OSStatus](errsecinvalididlinkage.md)
  The ID linkage is not valid.
- [var errSecInvalidIdentifier: OSStatus](errsecinvalididentifier.md)
  The identifier is not valid.
- [var errSecInvalidIndex: OSStatus](errsecinvalidindex.md)
  The index is not valid.
- [var errSecInvalidIndexInfo: OSStatus](errsecinvalidindexinfo.md)
  The index information is not valid.
- [var errSecInvalidInputVector: OSStatus](errsecinvalidinputvector.md)
  The input vector is not valid.
- [var errSecInvalidLoginName: OSStatus](errsecinvalidloginname.md)
  An invalid login name was detected.
- [var errSecInvalidModifyMode: OSStatus](errsecinvalidmodifymode.md)
  The modify mode is not valid.
- [var errSecInvalidName: OSStatus](errsecinvalidname.md)
  An invalid name was detected.
- [var errSecInvalidNetworkAddress: OSStatus](errsecinvalidnetworkaddress.md)
  An invalid network address was detected.
- [var errSecInvalidNewOwner: OSStatus](errsecinvalidnewowner.md)
  The new owner is not valid.
- [var errSecInvalidNumberOfFields: OSStatus](errsecinvalidnumberoffields.md)
  An invalid number of fields were detected.
- [var errSecInvalidOutputVector: OSStatus](errsecinvalidoutputvector.md)
  The output vector is not valid.
- [var errSecInvalidOwnerEdit: OSStatus](errsecinvalidowneredit.md)
  An invalid attempt to change the owner of an item.
- [var errSecInvalidPVC: OSStatus](errsecinvalidpvc.md)
  An invalid pointer validation checking policy was detected.
- [var errSecInvalidParsingModule: OSStatus](errsecinvalidparsingmodule.md)
  The parsing module is not valid.
- [var errSecInvalidPassthroughID: OSStatus](errsecinvalidpassthroughid.md)
  An invalid passthrough ID was detected.
- [var errSecInvalidPasswordRef: OSStatus](errsecinvalidpasswordref.md)
  The password reference is invalid.
- [var errSecInvalidPointer: OSStatus](errsecinvalidpointer.md)
  An invalid pointer was detected.
- [var errSecInvalidPolicyIdentifiers: OSStatus](errsecinvalidpolicyidentifiers.md)
  The policy identifiers are not valid.
- [var errSecInvalidQuery: OSStatus](errsecinvalidquery.md)
  The specified query is not valid.
- [var errSecInvalidReason: OSStatus](errsecinvalidreason.md)
  The trust policy reason is not valid.
- [var errSecInvalidRecord: OSStatus](errsecinvalidrecord.md)
  An invalid record was detected.
- [var errSecInvalidRequestInputs: OSStatus](errsecinvalidrequestinputs.md)
  The request inputs are not valid.
- [var errSecInvalidRequestor: OSStatus](errsecinvalidrequestor.md)
  The requestor is not valid.
- [var errSecInvalidResponseVector: OSStatus](errsecinvalidresponsevector.md)
  The response vector is not valid.
- [var errSecInvalidRoot: OSStatus](errsecinvalidroot.md)
  The root or anchor certificate is not valid.
- [var errSecInvalidSampleValue: OSStatus](errsecinvalidsamplevalue.md)
  An invalid sample value was detected.
- [var errSecInvalidScope: OSStatus](errsecinvalidscope.md)
  An invalid scope was detected.
- [var errSecInvalidServiceMask: OSStatus](errsecinvalidservicemask.md)
  An invalid service mask was detected.
- [var errSecInvalidSignature: OSStatus](errsecinvalidsignature.md)
  An invalid signature was detected.
- [var errSecInvalidStopOnPolicy: OSStatus](errsecinvalidstoponpolicy.md)
  The stop-on policy is not valid.
- [var errSecInvalidSubServiceID: OSStatus](errsecinvalidsubserviceid.md)
  An invalid sub-service ID was detected.
- [var errSecInvalidSubjectKeyID: OSStatus](errsecinvalidsubjectkeyid.md)
  The subject key ID is not valid.
- [var errSecInvalidTimeString: OSStatus](errsecinvalidtimestring.md)
  The time specified is not valid.
- [var errSecInvalidTrustSetting: OSStatus](errsecinvalidtrustsetting.md)
  The trust setting is invalid.
- [var errSecInvalidTrustSettings: OSStatus](errsecinvalidtrustsettings.md)
  The trust settings record is corrupted.
- [var errSecInvalidTuple: OSStatus](errsecinvalidtuple.md)
  The tuple is not valid.
- [var errSecInvalidTupleCredendtials: OSStatus](errsecinvalidtuplecredendtials.md)
  The tuple credentials are not valid.
- [var errSecInvalidTupleGroup: OSStatus](errsecinvalidtuplegroup.md)
  The tuple group is not valid.
- [var errSecInvalidValidityPeriod: OSStatus](errsecinvalidvalidityperiod.md)
  The validity period is not valid.
- [var errSecInvalidValue: OSStatus](errsecinvalidvalue.md)
  An invalid value was detected.
### Unsupported input result codes
- [var errSecUnsupportedAddressType: OSStatus](errsecunsupportedaddresstype.md)
  The address type is not supported.
- [var errSecUnsupportedFieldFormat: OSStatus](errsecunsupportedfieldformat.md)
  The field format is not supported.
- [var errSecUnsupportedFormat: OSStatus](errsecunsupportedformat.md)
  The specified import or export format is not supported.
- [var errSecUnsupportedIndexInfo: OSStatus](errsecunsupportedindexinfo.md)
  The index information is not supported.
- [var errSecUnsupportedLocality: OSStatus](errsecunsupportedlocality.md)
  The locality is not supported.
- [var errSecUnsupportedNumAttributes: OSStatus](errsecunsupportednumattributes.md)
  The number of attributes is not supported.
- [var errSecUnsupportedNumIndexes: OSStatus](errsecunsupportednumindexes.md)
  The number of indexes is not supported.
- [var errSecUnsupportedNumRecordTypes: OSStatus](errsecunsupportednumrecordtypes.md)
  The number of record types is not supported.
- [var errSecUnsupportedNumSelectionPreds: OSStatus](errsecunsupportednumselectionpreds.md)
  The number of selection predicates is not supported.
- [var errSecUnsupportedOperator: OSStatus](errsecunsupportedoperator.md)
  The operator is not supported.
- [var errSecUnsupportedQueryLimits: OSStatus](errsecunsupportedquerylimits.md)
  The query limits are not supported.
- [var errSecUnsupportedService: OSStatus](errsecunsupportedservice.md)
  The service is not supported.
- [var errSecUnsupportedVectorOfBuffers: OSStatus](errsecunsupportedvectorofbuffers.md)
  The vector of buffers is not supported.
### Apple specific result codes
- [var errSecAppleInvalidKeyEndDate: OSStatus](errsecappleinvalidkeyenddate.md)
  The specified key has an invalid end date.
- [var errSecAppleInvalidKeyStartDate: OSStatus](errsecappleinvalidkeystartdate.md)
  The specified key has an invalid start date.
- [var errSecApplePublicKeyIncomplete: OSStatus](errsecapplepublickeyincomplete.md)
  The public key is incomplete.
- [var errSecAppleSSLv2Rollback: OSStatus](errsecapplesslv2rollback.md)
  A SSLv2 rollback error has occurred.
- [var errSecAppleSignatureMismatch: OSStatus](errsecapplesignaturemismatch.md)
  A signature mismatch has occurred.
### Module manager result codes
- [var errSecEMMLoadFailed: OSStatus](errsecemmloadfailed.md)
  The elective module manager load failed.
- [var errSecEMMUnloadFailed: OSStatus](errsecemmunloadfailed.md)
  The elective module manager unload has failed.
- [var errSecModuleManagerInitializeFailed: OSStatus](errsecmodulemanagerinitializefailed.md)
  A module failed to initialize.
- [var errSecModuleManagerNotFound: OSStatus](errsecmodulemanagernotfound.md)
  A module was not found.
- [var errSecModuleManifestVerifyFailed: OSStatus](errsecmodulemanifestverifyfailed.md)
  A module manifest verification failure occurred.
- [var errSecModuleNotLoaded: OSStatus](errsecmodulenotloaded.md)
  A module was not loaded.
### Other Result Codes
- [var errSecAddinLoadFailed: OSStatus](errsecaddinloadfailed.md)
  The add-in load operation failed.
- [var errSecAddinUnloadFailed: OSStatus](errsecaddinunloadfailed.md)
  The add-in unload operation failed.
- [var errSecAlgorithmMismatch: OSStatus](errsecalgorithmmismatch.md)
  An algorithm mismatch occurred.
- [var errSecAlreadyLoggedIn: OSStatus](errsecalreadyloggedin.md)
  The user is already logged in.
- [var errSecAttachHandleBusy: OSStatus](errsecattachhandlebusy.md)
  The CSP handle was busy.
- [var errSecAttributeNotInContext: OSStatus](errsecattributenotincontext.md)
  An attribute was not in the context.
- [var errSecBlockSizeMismatch: OSStatus](errsecblocksizemismatch.md)
  A block size mismatch occurred.
- [var errSecCallbackFailed: OSStatus](errseccallbackfailed.md)
  A callback failed.
- [var errSecConversionError: OSStatus](errsecconversionerror.md)
  A conversion error has occurred.
- [var errSecDatabaseLocked: OSStatus](errsecdatabaselocked.md)
  The database is locked.
- [var errSecDatastoreIsOpen: OSStatus](errsecdatastoreisopen.md)
  The data store is open.
- [var errSecDecode: OSStatus](errsecdecode.md)
  Unable to decode the provided data.
- [var errSecDeviceError: OSStatus](errsecdeviceerror.md)
  A device error was encountered.
- [var errSecDeviceFailed: OSStatus](errsecdevicefailed.md)
  A device failure has occurred.
- [var errSecDeviceReset: OSStatus](errsecdevicereset.md)
  A device reset has occurred.
- [var errSecDeviceVerifyFailed: OSStatus](errsecdeviceverifyfailed.md)
  A device verification failure has occurred.
- [var errSecEventNotificationCallbackNotFound: OSStatus](errseceventnotificationcallbacknotfound.md)
  An event notification callback was not found.
- [var errSecExtendedKeyUsageNotCritical: OSStatus](errsecextendedkeyusagenotcritical.md)
  The extended key usage extension was not marked critical.
- [var errSecFieldSpecifiedMultiple: OSStatus](errsecfieldspecifiedmultiple.md)
  Too many fields were specified.
- [var errSecFileTooBig: OSStatus](errsecfiletoobig.md)
  The file is too big.
- [var errSecFunctionFailed: OSStatus](errsecfunctionfailed.md)
  A function has failed.
- [var errSecFunctionIntegrityFail: OSStatus](errsecfunctionintegrityfail.md)
  A function address is not within the verified module.
- [var errSecHostNameMismatch: OSStatus](errsechostnamemismatch.md)
  A host name mismatch has occurred.
- [var errSecIncompatibleDatabaseBlob: OSStatus](errsecincompatibledatabaseblob.md)
  The specified database has an incompatible blob.
- [var errSecIncompatibleFieldFormat: OSStatus](errsecincompatiblefieldformat.md)
  The field format is incompatible.
- [var errSecIncompatibleKeyBlob: OSStatus](errsecincompatiblekeyblob.md)
  The specified database has an incompatible key blob.
- [var errSecIncompatibleVersion: OSStatus](errsecincompatibleversion.md)
  The version is incompatible.
- [var errSecInputLengthError: OSStatus](errsecinputlengtherror.md)
  An input length error occurred.
- [var errSecInsufficientClientID: OSStatus](errsecinsufficientclientid.md)
  The client ID is incorrect.
- [var errSecInsufficientCredentials: OSStatus](errsecinsufficientcredentials.md)
  Insufficient credentials were detected.
- [var errSecInvalidAccessCredentials: OSStatus](errsecinvalidaccesscredentials.md)
  Invalid access credentials were detected.
- [var errSecInvalidAccessRequest: OSStatus](errsecinvalidaccessrequest.md)
  The access request is invalid.
- [var errSecLibraryReferenceNotFound: OSStatus](errseclibraryreferencenotfound.md)
  A library reference was not found.
- [var errSecMDSError: OSStatus](errsecmdserror.md)
  A module directory service error occurred.
- [var errSecMemoryError: OSStatus](errsecmemoryerror.md)
  A memory error occurred.
- [var errSecMissingEntitlement: OSStatus](errsecmissingentitlement.md)
  A required entitlement is missing.
- [var errSecMissingRequiredExtension: OSStatus](errsecmissingrequiredextension.md)
  A required certificate extension is missing.
- [var errSecMissingValue: OSStatus](errsecmissingvalue.md)
  A missing value was detected.
- [var errSecMultiplePrivKeys: OSStatus](errsecmultipleprivkeys.md)
  An attempt was made to import multiple private keys.
- [var errSecMultipleValuesUnsupported: OSStatus](errsecmultiplevaluesunsupported.md)
  Multiple values are not supported.
- [var errSecNoAccessForItem: OSStatus](errsecnoaccessforitem.md)
  The specified item has no access control.
- [var errSecNoBasicConstraints: OSStatus](errsecnobasicconstraints.md)
  No basic constraints were found.
- [var errSecNoBasicConstraintsCA: OSStatus](errsecnobasicconstraintsca.md)
  No basic CA constraints were found.
- [var errSecNoDefaultAuthority: OSStatus](errsecnodefaultauthority.md)
  No default authority was detected.
- [var errSecNoFieldValues: OSStatus](errsecnofieldvalues.md)
  No field values were detected.
- [var errSecNoTrustSettings: OSStatus](errsecnotrustsettings.md)
  No trust settings were found.
- [var errSecNotInitialized: OSStatus](errsecnotinitialized.md)
  A function was called without initializing the common security services manager.
- [var errSecNotLoggedIn: OSStatus](errsecnotloggedin.md)
  You are not logged in.
- [var errSecNotSigner: OSStatus](errsecnotsigner.md)
  The certificate is not signed by its proposed parent.
- [var errSecNotTrusted: OSStatus](errsecnottrusted.md)
  The trust policy is not trusted.
- [var errSecOutputLengthError: OSStatus](errsecoutputlengtherror.md)
  An output length error was detected.
- [var errSecPVCAlreadyConfigured: OSStatus](errsecpvcalreadyconfigured.md)
  The PVC is already configured.
- [var errSecPVCReferentNotFound: OSStatus](errsecpvcreferentnotfound.md)
  A reference to the calling module was not found in the list of authorized callers.
- [var errSecPassphraseRequired: OSStatus](errsecpassphraserequired.md)
  A password is required for import or export.
- [var errSecPathLengthConstraintExceeded: OSStatus](errsecpathlengthconstraintexceeded.md)
  The path length constraint was exceeded.
- [var errSecPkcs12VerifyFailure: OSStatus](errsecpkcs12verifyfailure.md)
  MAC verification failed during PKCS12 Import.
- [var errSecPolicyNotFound: OSStatus](errsecpolicynotfound.md)
  The specified policy cannot be found.
- [var errSecPrivilegeNotGranted: OSStatus](errsecprivilegenotgranted.md)
  The privilege is not granted.
- [var errSecPrivilegeNotSupported: OSStatus](errsecprivilegenotsupported.md)
  The privilege is not supported.
- [var errSecPublicKeyInconsistent: OSStatus](errsecpublickeyinconsistent.md)
  The public key is inconsistent.
- [var errSecQuerySizeUnknown: OSStatus](errsecquerysizeunknown.md)
  The query size is unknown.
- [var errSecQuotaExceeded: OSStatus](errsecquotaexceeded.md)
  The quota was exceeded.
- [var errSecRejectedForm: OSStatus](errsecrejectedform.md)
  The trust policy has a rejected form.
- [var errSecRequestDescriptor: OSStatus](errsecrequestdescriptor.md)
  The request descriptor is not valid.
- [var errSecRequestLost: OSStatus](errsecrequestlost.md)
  The request is lost.
- [var errSecRequestRejected: OSStatus](errsecrequestrejected.md)
  The request is rejected.
- [var errSecSelfCheckFailed: OSStatus](errsecselfcheckfailed.md)
  Self-check failed.
- [var errSecServiceNotAvailable: OSStatus](errsecservicenotavailable.md)
  Self-check failed.
- [var errSecStagedOperationInProgress: OSStatus](errsecstagedoperationinprogress.md)
  A staged operation is in progress.
- [var errSecStagedOperationNotStarted: OSStatus](errsecstagedoperationnotstarted.md)
  A staged operation was not started.
- [var errSecTagNotFound: OSStatus](errsectagnotfound.md)
  The specified tag is not found.
- [var errSecTrustNotAvailable: OSStatus](errsectrustnotavailable.md)
  No trust results are available.
- [var errSecUnknownFormat: OSStatus](errsecunknownformat.md)
  The item you are trying to import has an unknown format.
- [var errSecUnknownTag: OSStatus](errsecunknowntag.md)
  An unknown tag was detected.
- [var errSecVerificationFailure: OSStatus](errsecverificationfailure.md)
  A verification failure occurred.
- [var errSecVerifyActionFailed: OSStatus](errsecverifyactionfailed.md)
  A verify action failed.
- [var errSecVerifyFailed: OSStatus](errsecverifyfailed.md)
  A cryptographic verification failure occurred.

## See Also

- [Sessions API Result Codes](sessions-api-result-codes.md)
  Recognize result codes specific to the sessions API.
- [Secure Transport Result Codes](secure-transport-result-codes.md)
  Recognize result codes specific to the secure transport API.
- [Code Signing Services Result Codes](code-signing-services-result-codes.md)
  Recognize result codes specific to the code signing services API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/security-framework-result-codes)*