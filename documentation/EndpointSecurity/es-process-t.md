# es_process_t

**Framework**: Endpoint Security  
**Kind**: struct

A type that describes a process, as delivered by an Endpoint Security message.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_process_t
```

#### Overview

For process events, this type also indicates the newly-executing process.

You can extract values such as the process identifier (`PID`), user identifier (`UID`), and group identifier (`GID`) from the [`audit_token`](es_process_t/audit_token.md) field by using functions defined in `libbsm.h`.

##### Working with Code Signing

Fields related to code signing, such as [`cdhash`](es_process_t/cdhash.md) and [`signing_id`](es_process_t/signing_id.md), reflect the state of the process at the time Endpoint Security generated the message. In the specific case of process execution, this is after the `exec` completes in the kernel, but before any code in the process starts executing. At that point, XNU has validated the signature itself and has verified that the `cdhash` is correct. This second validation means that the hash of all individual page hashes in the Code Directory match the signed `cdhash`, essentially verifying the signature wasn’t tampered with. However, XNU doesn’t verify individual page hashes until the binary executes and pages in the corresponding pages. XNU doesn’t determine a binary shows signs of tampering until the individual pages page in, at which point XNU updates the code signing flags.

Endpoint Security provides clients the current state of the CS flags in the [`codesigning_flags`](es_process_t/codesigning_flags.md) member of the [`es_process_t`](es_process_t.md) structure. Keep the following points in mind when evaluating this field:

- The `CS_VALID` bit in [`codesigning_flags`](es_process_t/codesigning_flags.md) means that everything the kernel has validated up to that point in time was valid. However, this doesn’t mean there’s been a full validation of all the pages in the executable file. If a page’s content has been tampered with, XNU won’t know until that page pages in.
- When XNU detects a tampered page, it clears the `CS_VALID` bit. With the `CS_KILL` bit set, Endpoint Security terminates the process, preventing the tampered code from executing. Platform binaries and binaries that opted into the hardened runtime typically have the `CS_KILL` bit set.
- If you want your Endpoint Security client to detect tampered code before it pages in, such as at execution time, you can do so with the [`Security`](https://developer.apple.com/documentation/Security) framework. However, this may impose a significant performance cost.
- Endpoint Security plays no role in verifying the validity of code signatures.

## Topics

### Inspecting the Source Process
- [var audit_token: audit_token_t](es_process_t/audit_token.md)
  A token for use with Basic Security Module auditing functions.
- [var executable: UnsafeMutablePointer<es_file_t>](es_process_t/executable.md)
  The file containing the executed process.
- [var is_es_client: Bool](es_process_t/is_es_client.md)
  A Boolean value that indicates whether the process connects to the Endpoint Security subsystem.
- [var is_platform_binary: Bool](es_process_t/is_platform_binary.md)
  A Boolean value that indicates whether the process is a platform binary.
- [var start_time: timeval](es_process_t/start_time.md)
  The time the process started.
### Inspecting Process IDs
- [var ppid: pid_t](es_process_t/ppid.md)
  The parent process identifier.
- [var original_ppid: pid_t](es_process_t/original_ppid.md)
  The original parent process ID.
- [var group_id: pid_t](es_process_t/group_id.md)
  The process group identifier.
- [var session_id: pid_t](es_process_t/session_id.md)
  The identifier of the session that contains the process group.
- [var tty: UnsafeMutablePointer<es_file_t>?](es_process_t/tty.md)
  The TTY associated with the process sending the message.
### Inspecting Code Signing Properties
- [var codesigning_flags: UInt32](es_process_t/codesigning_flags.md)
  The flags used to sign the process.
- [var cdhash: es_cdhash_t](es_process_t/cdhash.md)
  The code directory hash value.
- [var signing_id: es_string_token_t](es_process_t/signing_id.md)
  The identifier used to sign the process.
- [var team_id: es_string_token_t](es_process_t/team_id.md)
  The team identifier used to sign the process.
### Inspecting Audit Tokens
- [var responsible_audit_token: audit_token_t](es_process_t/responsible_audit_token.md)
  The audit token of the process responsible for this process.
- [var parent_audit_token: audit_token_t](es_process_t/parent_audit_token.md)
  The audit token of the parent process.
### Initializers
- [init(audit_token: audit_token_t, ppid: pid_t, original_ppid: pid_t, group_id: pid_t, session_id: pid_t, codesigning_flags: UInt32, is_platform_binary: Bool, is_es_client: Bool, cdhash: es_cdhash_t, signing_id: es_string_token_t, team_id: es_string_token_t, executable: UnsafeMutablePointer<es_file_t>, tty: UnsafeMutablePointer<es_file_t>?, start_time: timeval, responsible_audit_token: audit_token_t, parent_audit_token: audit_token_t, cs_validation_category: es_cs_validation_category_t)](es_process_t/init(audit_token:ppid:original_ppid:group_id:session_id:codesigning_flags:is_platform_binary:is_es_client:cdhash:signing_id:team_id:executable:tty:start_time:responsible_audit_token:parent_audit_token:cs_validation_category:).md)
### Instance Properties
- [var cs_validation_category: es_cs_validation_category_t](es_process_t/cs_validation_category.md)
  es_cs_validation_category

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [var target: UnsafeMutablePointer<es_process_t>](es_event_exec_t/target.md)
  The process to execute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t)*