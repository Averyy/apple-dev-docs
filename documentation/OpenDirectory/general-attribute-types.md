# General Attribute Types

**Framework**: Open Directory

Types of Open Directory attributes.

## Topics

### Constants
- [let kODAttributeTypeAllAttributes: String](kodattributetypeallattributes.md)
  The attribute type used in requesting all attribute types in a search.
- [let kODAttributeTypeStandardOnly: String](kodattributetypestandardonly.md)
  The attribute type used in requesting only standard attribute types in a search.
- [let kODAttributeTypeNativeOnly: String](kodattributetypenativeonly.md)
  The attribute type used in requesting only native attribute types in a search.
- [let kODAttributeTypeAdminLimits: String](kodattributetypeadminlimits.md)
  The attribute type of an XML property list that indicates what an admin user can edit. Found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeAuthenticationHint: String](kodattributetypeauthenticationhint.md)
  The attribute type of an authentication hint attribute.
- [let kODAttributeTypeAllTypes: String](kodattributetypealltypes.md)
  The attribute type used to indicate all attribute types for a given record type the config node.
- [let kODAttributeTypeAuthorityRevocationList: String](kodattributetypeauthorityrevocationlist.md)
  The attribute type of the authority revocation list attribute, which defines certificate authority certificates that are no longer trusted. Typically found in records of type `kODRecordTypeCertificateAuthorities`.
- [let kODAttributeTypeBirthday: String](kodattributetypebirthday.md)
  The attribute type of a birthday attribute.
- [let kODAttributeTypeCACertificate: String](kodattributetypecacertificate.md)
  The attribute type of a certificate authority certificate attribute, which contains the binary of the certificate. Typically found in records of type `kODRecordTypeCertificateAuthority`.
- [let kODAttributeTypeCapacity: String](kodattributetypecapacity.md)
  The attribute type of a capacity attribute, which indicates the capacity of a resource.
- [let kODAttributeTypeCertificateRevocationList: String](kodattributetypecertificaterevocationlist.md)
  The attribute type of the certificate revocation list attribute, which defines certificates that are no longer trusted. Typically found in records of type `kODRecordTypeCertificateAuthorities`.
- [let kODAttributeTypeComment: String](kodattributetypecomment.md)
  The attribute type of an unformatted comment attribute.
- [let kODAttributeTypeContactGUID: String](kodattributetypecontactguid.md)
  The attribute type of the contact GUID attribute. Typically found in records of type `kODRecordTypeGroups`.
- [let kODAttributeTypeContactPerson: String](kodattributetypecontactperson.md)
  The attribute type of the contact person attribute, which indicates the contact person of a machine.
- [let kODAttributeTypeCreationTimestamp: String](kodattributetypecreationtimestamp.md)
  The attribute type of the creation timestamp attribute, which indicates the time the record was created.
- [let kODAttributeTypeCrossCertificatePair: String](kodattributetypecrosscertificatepair.md)
  The attribute type of the cross certificate attribute, which contains the binary of two certificates that verify one another. Typically found in records of type `kODRecordTypeCertificateAuthorities`
- [let kODAttributeTypeDataStamp: String](kodattributetypedatastamp.md)
  The attribute type of the data stamp attribute, which is used for checksum and accessing metadata.
- [let kODAttributeTypeFullName: String](kodattributetypefullname.md)
  The attribute type of the full name attribute, which indicates the full name of the record.
- [let kODAttributeTypeDNSDomain: String](kodattributetypednsdomain.md)
  The attribute type of the DNS domain attribute.
- [let kODAttributeTypeDNSNameServer: String](kodattributetypednsnameserver.md)
  The attribute type of the DNS name server attribute.
- [let kODAttributeTypeENetAddress: String](kodattributetypeenetaddress.md)
  The attribute type of the ethernet address attribute, which specifies a record’s ethernet address (MAC address).
- [let kODAttributeTypeExpire: String](kodattributetypeexpire.md)
  The attribute type of the expiration attribute, which indicates the expiration date or time of a record.
- [let kODAttributeTypeFirstName: String](kodattributetypefirstname.md)
  The attribute type of the first name attribute.
- [let kODAttributeTypeGUID: String](kodattributetypeguid.md)
  The attribute type of the GUID attribute, which indicates a record’s 128-bit GUID.
- [let kODAttributeTypeHomeDirectoryQuota: String](kodattributetypehomedirectoryquota.md)
  The attribute type of the home directory quota attribute, which is listed in bytes. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeHomeDirectorySoftQuota: String](kodattributetypehomedirectorysoftquota.md)
  The attribute type of the home directory soft quota attribute, which is listed in bytes. This specifies a size limit at which users are notified that they are reaching their hard quota. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeHomeLocOwner: String](kodattributetypehomelocowner.md)
  The attribute type of the workgroup shared home directory attribute.
- [let kODAttributeTypeInternetAlias: String](kodattributetypeinternetalias.md)
  The attribute type of the internet alias attribute.
- [let kODAttributeTypeKDCConfigData: String](kodattributetypekdcconfigdata.md)
  The attribute type of the KDC configuration file attribute.
- [let kODAttributeTypeKerberosServices: String](kodattributetypekerberosservices.md)
  The attribute type of the Kerberos services attribute.
- [let kODAttributeTypeLastName: String](kodattributetypelastname.md)
  The attribute type of the last name attribute.
- [let kODAttributeTypeLDAPSearchBaseSuffix: String](kodattributetypeldapsearchbasesuffix.md)
  The attribute type of the LDAP server search base suffix attribute.
- [let kODAttributeTypeLocation: String](kodattributetypelocation.md)
  The attribute type of the location attribute, which indicates the domain names a service is available from. Typically found in service record types, such as `kODRecordTypeAFPServer`, `kODRecordTypeLDAPServer`, and `kODRecordTypeWebServer`.
- [let kODAttributeTypeMapGUID: String](kodattributetypemapguid.md)
  The attribute type of the map GUID attribute.
- [let kODAttributeTypeMCXFlags: String](kodattributetypemcxflags.md)
  The attribute type of the MCX flags attribute.
- [let kODAttributeTypeMCXSettings: String](kodattributetypemcxsettings.md)
  The attribute type of the MCX settings attribute.
- [let kODAttributeTypeMailAttribute: String](kodattributetypemailattribute.md)
  The attribute type of the mail attribute, which contains mail account configuration data.
- [let kODAttributeTypeMetaAutomountMap: String](kodattributetypemetaautomountmap.md)
  The attribute type used to query for records of type `kODRecordTypeAutomount` that are associated with a specific record of type `kODRecordTypeAutomountMap`.
- [let kODAttributeTypeMiddleName: String](kodattributetypemiddlename.md)
  The attribute type of the middle name attribute.
- [let kODAttributeTypeModificationTimestamp: String](kodattributetypemodificationtimestamp.md)
  The attribute type of the modification timestamp attribute, which indicates the time the record was last modified.
- [let kODAttributeTypeNFSHomeDirectory: String](kodattributetypenfshomedirectory.md)
  The attribute type of the NFS home directory attribute.
- [let kODAttributeTypeNote: String](kodattributetypenote.md)
  The attribute type of the last name attribute.
- [let kODAttributeTypeOwner: String](kodattributetypeowner.md)
  The attribute type of the owner attribute.
- [let kODAttributeTypeOwnerGUID: String](kodattributetypeownerguid.md)
  The attribute type of the owner GUID attribute. Typically found in records of type `kODRecordTypeGroups`.
- [let kODAttributeTypePassword: String](kodattributetypepassword.md)
  The attribute type of the password attribute.
- [let kODAttributeTypePasswordPlus: String](kodattributetypepasswordplus.md)
  The attribute type of the attribute that holds marker data to indicate possible authentication redirection.
- [let kODAttributeTypePasswordPolicyOptions: String](kodattributetypepasswordpolicyoptions.md)
  The attribute type of the password policy options attribute. Typically found in records of type `kODRecordTypePresetUsers`.
- [let kODAttributeTypePasswordServerList: String](kodattributetypepasswordserverlist.md)
  The attribute type of the password server list attribute, which contains the password server’s replication information.
- [let kODAttributeTypePasswordServerLocation: String](kodattributetypepasswordserverlocation.md)
  The attribute type of the password server location attribute, which specifies the IP address or domain name of the password server associated with a given directory node.
- [let kODAttributeTypePicture: String](kodattributetypepicture.md)
  The attribute type of the picture attribute, which specifies the path of the picture for each user displayed in the login window.
- [let kODAttributeTypePort: String](kodattributetypeport.md)
  The attribute type of the port attribute, which indicates the port number a service is available on.
- [let kODAttributeTypePresetUserIsAdmin: String](kodattributetypepresetuserisadmin.md)
  The attribute type used to indicate whether users created from a given preset are administrators. Typically found in records of type `kODRecordTypePresetUsers`.
- [let kODAttributeTypePrimaryComputerGUID: String](kodattributetypeprimarycomputerguid.md)
  The attribute type used to define the primary computer of a computer group. Typically found in records of type kODRecordTypeComputerGroups
- [let kODAttributeTypePrimaryComputerList: String](kodattributetypeprimarycomputerlist.md)
  The attribute type of the primary computer list attribute, which indicates the computer list a given computer record is associated with.
- [let kODAttributeTypePrimaryGroupID: String](kodattributetypeprimarygroupid.md)
  The attribute type used to define a user’s primary group.
- [let kODAttributeTypePrinter1284DeviceID: String](kodattributetypeprinter1284deviceid.md)
  The attribute type used to define a printer’s IEEE 1284 device ID.
- [let kODAttributeTypePrinterLPRHost: String](kodattributetypeprinterlprhost.md)
  The attribute type used to define a printer’s LPR host.
- [let kODAttributeTypePrinterLPRQueue: String](kodattributetypeprinterlprqueue.md)
  The attribute type used to define a printer’s LPR queue.
- [let kODAttributeTypePrinterMakeAndModel: String](kodattributetypeprintermakeandmodel.md)
  The attribute type used to define a printer’s make and model. Based on the IPP Printing Specification RFC and IETF IPP-LDAP Printer Record.
- [let kODAttributeTypePrinterType: String](kodattributetypeprintertype.md)
  The attribute type used to define a printer’s type.
- [let kODAttributeTypePrinterURI: String](kodattributetypeprinteruri.md)
  The attribute type used to define a printer’s URI. Based on the IPP Printing Specification RFC and IETF IPP-LDAP Printer Record.
- [let kODAttributeTypePrinterXRISupported: String](kodattributetypeprinterxrisupported.md)
  The attribute type used to define additional URIs supported by a printer. Based on the IPP Printing Specification RFC and IETF IPP-LDAP Printer Record.
- [let kODAttributeTypePrintServiceInfoText: String](kodattributetypeprintserviceinfotext.md)
  The attribute type used to define a printer’s service info in plaintext.
- [let kODAttributeTypePrintServiceInfoXML: String](kodattributetypeprintserviceinfoxml.md)
  The attribute type used to define a printer’s service info in XML.
- [let kODAttributeTypePrintServiceUserData: String](kodattributetypeprintserviceuserdata.md)
  The attribute type used to define a printer’s quota configuration and statistics in XML. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePrintServiceUser`.
- [let kODAttributeTypeRealUserID: String](kodattributetyperealuserid.md)
  The attribute type of the real user ID attribute, which is used by Managed Client.
- [let kODAttributeTypeRelativeDNPrefix: String](kodattributetyperelativednprefix.md)
  The attribute type used to map the first native LDAP attribute type needed for building a relative distinguished name.
- [let kODAttributeTypeSMBAcctFlags: String](kodattributetypesmbacctflags.md)
  The attribute type used as an account control flag.
- [let kODAttributeTypeSMBGroupRID: String](kodattributetypesmbgrouprid.md)
  The attribute type used to define PDC SMB interaction with DirectoryService.
- [let kODAttributeTypeSMBHome: String](kodattributetypesmbhome.md)
  The attribute type used to define the UNC address of a Windows home directory mount point.
- [let kODAttributeTypeSMBHomeDrive: String](kodattributetypesmbhomedrive.md)
  The attribute type used to define the drive letter of a Windows home directory mount point.
- [let kODAttributeTypeSMBKickoffTime: String](kodattributetypesmbkickofftime.md)
  The attribute type used to define kickoff time in SMB interaction.
- [let kODAttributeTypeSMBLogoffTime: String](kodattributetypesmblogofftime.md)
  The attribute type used to define logoff time in SMB interaction.
- [let kODAttributeTypeSMBLogonTime: String](kodattributetypesmblogontime.md)
  The attribute type used to define logon time in SMB interaction.
- [let kODAttributeTypeSMBPrimaryGroupSID: String](kodattributetypesmbprimarygroupsid.md)
  The attribute type used to define an SMB primary group’s security ID, which is stored as a string of up to 64 bytes.
- [let kODAttributeTypeSMBPWDLastSet: String](kodattributetypesmbpwdlastset.md)
  An attribute type used in SMB interaction.
- [let kODAttributeTypeSMBProfilePath: String](kodattributetypesmbprofilepath.md)
  The attribute type used to define desktop management information.
- [let kODAttributeTypeSMBRID: String](kodattributetypesmbrid.md)
  An attribute type used in SMB interaction.
- [let kODAttributeTypeSMBScriptPath: String](kodattributetypesmbscriptpath.md)
  The attribute type used to define an SMB login script path.
- [let kODAttributeTypeSMBSID: String](kodattributetypesmbsid.md)
  The attribute type used to define an SMB security ID, which is stored as a string of up to 64 bytes. Typically found in records of type `kODRecordTypeUsers`, `kODRecordTypeGroups`, and `kODRecordTypeComputers`.
- [let kODAttributeTypeSMBUserWorkstations: String](kodattributetypesmbuserworkstations.md)
  The attribute type used to define a list of workstations a user can log in from.
- [let kODAttributeTypeServiceType: String](kodattributetypeservicetype.md)
  The attribute type used to define an SMB login script path.
- [let kODAttributeTypeSetupAdvertising: String](kodattributetypesetupadvertising.md)
  The attribute type used to define the raw service type of a service. For instance, a service record of type `kODRecordTypeWebServer` could have a service of type `http` or `https`.
- [let kODAttributeTypeSetupAutoRegister: String](kodattributetypesetupautoregister.md)
  An attribute type used for automatic population in Setup Assistant.
- [let kODAttributeTypeSetupLocation: String](kodattributetypesetuplocation.md)
  An attribute type used for automatic population in Setup Assistant.
- [let kODAttributeTypeSetupOccupation: String](kodattributetypesetupoccupation.md)
  An attribute type used for automatic population in Setup Assistant.
- [let kODAttributeTypeTimeToLive: String](kodattributetypetimetolive.md)
  The attribute type used to specify how long to cache a record’s attribute values. Specified in seconds.
- [let kODAttributeTypeUniqueID: String](kodattributetypeuniqueid.md)
  The attribute type used to define a user’s unique 32-bit ID in the legacy manner.
- [let kODAttributeTypeUserCertificate: String](kodattributetypeusercertificate.md)
  The attribute type used to store the binary of a user’s certificate. Typically found in user records.
- [let kODAttributeTypeUserPKCS12Data: String](kodattributetypeuserpkcs12data.md)
  The attribute type used to store binary data in PKCS #12 format, including keys and certificates. Typically found in user records.
- [let kODAttributeTypeUserShell: String](kodattributetypeusershell.md)
  The attribute type used to specify a user’s shell setting.
- [let kODAttributeTypeUserSMIMECertificate: String](kodattributetypeusersmimecertificate.md)
  The attribute type used to store the binary of a user’s SMIME certificate. Typically found in user records.
- [let kODAttributeTypeVFSDumpFreq: String](kodattributetypevfsdumpfreq.md)
  An attribute type used to support mount records.
- [let kODAttributeTypeVFSLinkDir: String](kodattributetypevfslinkdir.md)
  An attribute type used to support mount records.
- [let kODAttributeTypeVFSPassNo: String](kodattributetypevfspassno.md)
  An attribute type used to support mount records.
- [let kODAttributeTypeVFSType: String](kodattributetypevfstype.md)
  An attribute type used to support mount records.
- [let kODAttributeTypeWeblogURI: String](kodattributetypewebloguri.md)
  The attribute type used to specify the URI of a user’s weblog.
- [let kODAttributeTypeXMLPlist: String](kodattributetypexmlplist.md)
  The attribute type used to specify an XML property list.
- [let kODAttributeTypeProtocolNumber: String](kodattributetypeprotocolnumber.md)
  The attribute type used to specify a protocol number. Typically found in records of type `kODRecordTypeProtocols`.
- [let kODAttributeTypeRPCNumber: String](kodattributetyperpcnumber.md)
  The attribute type used to specify an RPC number.
- [let kODAttributeTypeNetworkNumber: String](kodattributetypenetworknumber.md)
  The attribute type used to specify a network number. Typically found in records of type `kODRecordTypeNetworks`
- [let kODAttributeTypeAccessControlEntry: String](kodattributetypeaccesscontrolentry.md)
  The attribute type used to store directory access control directives.
- [let kODAttributeTypeAddressLine1: String](kodattributetypeaddressline1.md)
  The attribute type used to store the first line of a user’s address data.
- [let kODAttributeTypeAddressLine2: String](kodattributetypeaddressline2.md)
  The attribute type used to store the second line of a user’s address data.
- [let kODAttributeTypeAddressLine3: String](kodattributetypeaddressline3.md)
  The attribute type used to store the third line of a user’s address data.
- [let kODAttributeTypeAreaCode: String](kodattributetypeareacode.md)
  The attribute type used to store a user’s area code.
- [let kODAttributeTypeAuthenticationAuthority: String](kodattributetypeauthenticationauthority.md)
  The attribute type used to specify the mechanism used to verify or set a user’s password. Typically found in records of type `kODRecordTypeUsers`
- [let kODAttributeTypeAutomountInformation: String](kodattributetypeautomountinformation.md)
  The attribute type used to store automount information.
- [let kODAttributeTypeBootParams: String](kodattributetypebootparams.md)
  The attribute type used to store boot parameters. Typically found in host or machine records.
- [let kODAttributeTypeBuilding: String](kodattributetypebuilding.md)
  The attribute type used to store a user’s building information. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeServicesLocator: String](kodattributetypeserviceslocator.md)
  The attribute type used to specify the URI of a record’s calendar.
- [let kODAttributeTypeCity: String](kodattributetypecity.md)
  The attribute type used to store a user’s city information. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeCompany: String](kodattributetypecompany.md)
  The attribute type used to store a user’s company information. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeComputers: String](kodattributetypecomputers.md)
  The attribute type used to store a list of computers.
- [let kODAttributeTypeCountry: String](kodattributetypecountry.md)
  The attribute type used to store a user’s country or region information. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeDepartment: String](kodattributetypedepartment.md)
  The attribute type used to store a user’s department information. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeDNSName: String](kodattributetypednsname.md)
  The attribute type used to specify a DNS resolver nameserver.
- [let kODAttributeTypeEMailAddress: String](kodattributetypeemailaddress.md)
  The attribute type used to store a user’s email address. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeEMailContacts: String](kodattributetypeemailcontacts.md)
  The attribute type used to store a user’s custom email information. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeFaxNumber: String](kodattributetypefaxnumber.md)
  The attribute type used to store a user’s fax number. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeGroup: String](kodattributetypegroup.md)
  The attribute type used to store a list of groups.
- [let kODAttributeTypeGroupMembers: String](kodattributetypegroupmembers.md)
  The attribute type used to specify the GUID values of members of a group that are not groups.
- [let kODAttributeTypeGroupMembership: String](kodattributetypegroupmembership.md)
  The attribute type used to specify a list of users that belong to a given group.
- [let kODAttributeTypeGroupServices: String](kodattributetypegroupservices.md)
  The attribute type used to specify an XML property list that defines a group’s services. Typically found in records of type `kODRecordTypeGroups`.
- [let kODAttributeTypeHomePhoneNumber: String](kodattributetypehomephonenumber.md)
  The attribute type used to store a user’s home phone number. Typically found in records of type `kODRecordTypeUsers` or `kODRecordTypePeople`.
- [let kODAttributeTypeHTML: String](kodattributetypehtml.md)
  The attribute type used to specify an HTML location.
- [let kODAttributeTypeHomeDirectory: String](kodattributetypehomedirectory.md)
  The attribute type used to specify the allowed usage of a user’s home directory in bytes. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeIMHandle: String](kodattributetypeimhandle.md)
  The attribute type used to store a user’s instant messaging handles. Typically found in records of type `kODRecordTypeUsers`.
- [let kODAttributeTypeIPAddress: String](kodattributetypeipaddress.md)
  The attribute type used to specify an IP address.
- [let kODAttributeTypeIPAddressAndENetAddress: String](kodattributetypeipaddressandenetaddress.md)
  The attribute type used to specify a pairing of an IPv4 or IPv6 address with an ethernet address. Typically found in records of type `kODRecordTypeComputers`.
- [let kODAttributeTypeIPv6Address: String](kodattributetypeipv6address.md)
  The attribute type used to specify an IPv6 address. Typically found in records of type `kODRecordTypeComputers` and `kODRecordTypeHosts`.
- [let kODAttributeTypeJPEGPhoto: String](kodattributetypejpegphoto.md)
  The attribute type used to store binary picture data in JPEG format. Typically found in records of type `kODRecordTypeUsers`, `kODRecordTypePeople`, and `kODRecordTypeGroups`.
- [let kODAttributeTypeJobTitle: String](kodattributetypejobtitle.md)
  The attribute type used to store a user’s job title.
- [let kODAttributeTypeKDCAuthKey: String](kodattributetypekdcauthkey.md)
  The attribute type used to store a KDC primary key.
- [let kODAttributeTypeKeywords: String](kodattributetypekeywords.md)
  The attribute type used to specify keywords for search capability.
- [let kODAttributeTypeLDAPReadReplicas: String](kodattributetypeldapreadreplicas.md)
  The attribute type used to specify a list of LDAP server URLs that can be used to read directory data.
- [let kODAttributeTypeLDAPWriteReplicas: String](kodattributetypeldapwritereplicas.md)
  The attribute type used to specify a list of LDAP server URLs that can be used to write directory data.
- [let kODAttributeTypeMapCoordinates: String](kodattributetypemapcoordinates.md)
  The attribute type used to store coordinates of a user’s location.
- [let kODAttributeTypeMapURI: String](kodattributetypemapuri.md)
  The attribute type used to specify the URI of a user’s location.
- [let kODAttributeTypeMIME: String](kodattributetypemime.md)
  The attribute type used to store data of a fully qualified MIME type.
- [let kODAttributeTypeMobileNumber: String](kodattributetypemobilenumber.md)
  The attribute type used to store a user’s mobile phone information.
- [let kODAttributeTypeNestedGroups: String](kodattributetypenestedgroups.md)
  The attribute type used to specify a list of nested group GUID values in a group attribute.
- [let kODAttributeTypeNetGroups: String](kodattributetypenetgroups.md)
  The attribute type used to specify a list of net groups that a user or host record is a member of.
- [let kODAttributeTypeNickName: String](kodattributetypenickname.md)
  The attribute type used to store a user’s nickname.
- [let kODAttributeTypeOrganizationInfo: String](kodattributetypeorganizationinfo.md)
  The attribute type used to store a user’s organization information.
- [let kODAttributeTypeOrganizationName: String](kodattributetypeorganizationname.md)
  The attribute type used to store a user’s organization name.
- [let kODAttributeTypePagerNumber: String](kodattributetypepagernumber.md)
  The attribute type used to store a user’s pager number.
- [let kODAttributeTypePhoneContacts: String](kodattributetypephonecontacts.md)
  The attribute type used to store a user’s custom phone information.
- [let kODAttributeTypePhoneNumber: String](kodattributetypephonenumber.md)
  The attribute type used to store a user’s phone number.
- [let kODAttributeTypePGPPublicKey: String](kodattributetypepgppublickey.md)
  The attribute type used to specify a Pretty Good Privacy public key.
- [let kODAttributeTypePostalAddress: String](kodattributetypepostaladdress.md)
  The attribute type used to store a user’s postal address.
- [let kODAttributeTypePostalAddressContacts: String](kodattributetypepostaladdresscontacts.md)
  The attribute type used to store a user’s custom postal address information.
- [let kODAttributeTypePostalCode: String](kodattributetypepostalcode.md)
  The attribute type used to store a user’s postal code.
- [let kODAttributeTypeNamePrefix: String](kodattributetypenameprefix.md)
  The attribute type used to store a user’s title prefix.
- [let kODAttributeTypeProtocols: String](kodattributetypeprotocols.md)
  The attribute type used to specify a list of protocols.
- [let kODAttributeTypeRecordName: String](kodattributetyperecordname.md)
  The attribute type used to specify a list of names for a record.
- [let kODAttributeTypeRelationships: String](kodattributetyperelationships.md)
  The attribute type used to specify a user’s relationships.
- [let kODAttributeTypeResourceInfo: String](kodattributetyperesourceinfo.md)
  The attribute type used to specify resource record information.
- [let kODAttributeTypeResourceType: String](kodattributetyperesourcetype.md)
  The attribute type used to specify the type of a resource record.
- [let kODAttributeTypeState: String](kodattributetypestate.md)
  The attribute type used to specify a user’s state or province.
- [let kODAttributeTypeStreet: String](kodattributetypestreet.md)
  The attribute type used to specify a user’s street address.
- [let kODAttributeTypeNameSuffix: String](kodattributetypenamesuffix.md)
  The attribute type used to specify a user’s title suffix.
- [let kODAttributeTypeURL: String](kodattributetypeurl.md)
  The attribute type used to specify a list of URLs.
- [let kODAttributeTypeVFSOpts: String](kodattributetypevfsopts.md)
  An attribute type used to support mount records.
- [let kODAttributeTypeAlias: String](kodattributetypealias.md)
  The attribute type used to specify an alias that contains a pointer to another record, node, or attribute.
- [let kODAttributeTypeAuthCredential: String](kodattributetypeauthcredential.md)
  The attribute type used to store an authentication credential used to authenticate to a directory.
- [let kODAttributeTypeCopyTimestamp: String](kodattributetypecopytimestamp.md)
  The attribute type used to store a timestamp used in local account caching.
- [let kODAttributeTypeDateRecordCreated: String](kodattributetypedaterecordcreated.md)
  The attribute type used to store a record’s creation date.
- [let kODAttributeTypeKerberosRealm: String](kodattributetypekerberosrealm.md)
  An attribute type used to support Kerberos SMB server services.
- [let kODAttributeTypeNTDomainComputerAccount: String](kodattributetypentdomaincomputeraccount.md)
  An attribute type used to support Kerberos SMB server services.
- [let kODAttributeTypeOriginalHomeDirectory: String](kodattributetypeoriginalhomedirectory.md)
  The attribute type used to store a home directory URL used in local account caching.
- [let kODAttributeTypeOriginalNFSHomeDirectory: String](kodattributetypeoriginalnfshomedirectory.md)
  The attribute type used to store an NFS home directory URL used in local account caching.
- [let kODAttributeTypeOriginalNodeName: String](kodattributetypeoriginalnodename.md)
  The attribute type used to store a node name used in local account caching.
- [let kODAttributeTypePrimaryNTDomain: String](kodattributetypeprimaryntdomain.md)
  An attribute type used to support Kerberos SMB server services.
- [let kODAttributeTypePwdAgingPolicy: String](kodattributetypepwdagingpolicy.md)
  The attribute type used to store a record’s password aging policy.
- [let kODAttributeTypeReadOnlyNode: String](kodattributetypereadonlynode.md)
  The attribute type used to specify a read-only node.
- [let kODAttributeTypeTimePackage: String](kodattributetypetimepackage.md)
  The attribute type used to group a record’s creation, modification, and backup timestamps.
- [let kODAttributeTypeTotalSize: String](kodattributetypetotalsize.md)
  An attribute type used for checksum and accessing metadata.
- [let kODAttributeTypeAuthMethod: String](kodattributetypeauthmethod.md)
  The attribute type used to specify a record’s authentication method.
- [let kODAttributeTypeMetaNodeLocation: String](kodattributetypemetanodelocation.md)
  The attribute type used to retrieve the registered node name with the directory node plug-in.
- [let kODAttributeTypeNodePath: String](kodattributetypenodepath.md)
  The attribute type used in neighborhood records to specify the node to search while looking up aliases in the neighborhood.
- [let kODAttributeTypePlugInInfo: String](kodattributetypeplugininfo.md)
  The attribute type used to specify information about the plug-in that is serving a particular directory node.
- [let kODAttributeTypeRecordType: String](kodattributetyperecordtype.md)
  The attribute type used to specify the type of a record or a directory node.
- [let kODAttributeTypeSchema: String](kodattributetypeschema.md)
  The attribute type used to specify a record’s list of attribute types.
- [let kODAttributeTypeSubNodes: String](kodattributetypesubnodes.md)
  The attribute type used to specify a node’s list of subnodes.
- [let kODAttributeTypeNetGroupTriplet: String](kodattributetypenetgrouptriplet.md)
  The attribute type used to specify a node’s list of subnodes.
- [let kODAttributeTypeSearchPath: String](kodattributetypesearchpath.md)
  The attribute type used to specify the search path used by a search node.
- [let kODAttributeTypeSearchPolicy: String](kodattributetypesearchpolicy.md)
  The attribute type used to specify the search policy used by a search node.
- [let kODAttributeTypeAutomaticSearchPath: String](kodattributetypeautomaticsearchpath.md)
  The attribute type used to specify the automatic search path used by a search node.
- [let kODAttributeTypeLocalOnlySearchPath: String](kodattributetypelocalonlysearchpath.md)
  The attribute type used to specify the local-only search path used by a search node.
- [let kODAttributeTypeCustomSearchPath: String](kodattributetypecustomsearchpath.md)
  The attribute type used to specify an admin-configured search path used by a search node.
- [let kODAttributeTypeAdvertisedServices: String](kodattributetypeadvertisedservices.md)
  The attribute type used to specify (Bonjour) advertised services.
- [let kODAttributeTypeLocaleRelay: String](kodattributetypelocalerelay.md)
  The attribute type used to specify a relay server for a locale.
- [let kODAttributeTypeLocaleSubnets: String](kodattributetypelocalesubnets.md)
  The attribute type used to specify the subnets for a locale.
- [let kODAttributeTypeNetworkInterfaces: String](kodattributetypenetworkinterfaces.md)
  The attribute type used to specify network interfaces.
- [let kODAttributeTypeParentLocales: String](kodattributetypeparentlocales.md)
  The attribute type for specifying locales of the parent.
- [let kODAttributeTypePrimaryLocale: String](kodattributetypeprimarylocale.md)
  The attribute type for specifying the primary locale.

## See Also

- [Session Keys](session-keys.md)
  Keys used when specifying session information.
- [Node Types](1497602-node-types.md)
  Open Directory node types.
- [Match Types](match-types.md)
  Types of matches used for searches.
- [Record Types](record-types.md)
  Types of Open Directory records.
- [Configuration Attribute Types](configuration-attribute-types.md)
  Types of Open Directory attributes specifically for use with configure nodes.
- [Authentication Types](authentication-types.md)
  Types of authentication available in Open Directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/opendirectory/general-attribute-types)*